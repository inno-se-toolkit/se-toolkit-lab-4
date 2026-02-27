{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    devshell = {
      url = "github:deemp/devshell";
      inputs.nixpkgs.follows = "nixpkgs";
    };
    flake-parts.url = "github:hercules-ci/flake-parts";
    systems.url = "github:nix-systems/default";
  };

  outputs =
    inputs@{ flake-parts, ... }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      imports = [
        inputs.devshell.flakeModule
      ];
      systems = import inputs.systems;
      perSystem =
        { pkgs, ... }:
        let
          python = pkgs.python3.withPackages (ps: [ ps.pydantic ]);
        in
        {
          devshells.default = {
            bash.extra = ''
              export ROOT_DIR="$(pwd)"
            '';
            commandGroups = {
              "1-front-tools" = [
                pkgs.nodejs_22
              ];
              "2-back-tools" = [
                pkgs.uv
              ];
              "3-lint-scripts" = [
                {
                  name = "find-broken-links";
                  command = ''
                    ${pkgs.lib.getExe pkgs.lychee} \
                      --include-fragments \
                      --offline \
                      --no-progress \
                      --exclude-path '.venv' \
                      --exclude-path '.direnv' \
                      --exclude-path 'node_modules' \
                      --root-dir . \
                      --cache \
                      --format json \
                      "$ROOT_DIR"/'**/*.md' \
                      | ${pkgs.lib.getExe python} ${./instructors/scripts/find-broken-links/post-process-lychee.py}
                  '';
                  help = "Find all broken links in all Markdown files (with file:line locations)";
                }
                {
                  name = "lint-docs";
                  command = ''
                    ${pkgs.lib.getExe pkgs.markdownlint-cli2} \
                      '**/*.md' '#.direnv' '#.venv' '#node_modules'
                  '';
                  help = "Lint all Markdown files";
                }
              ];
              "4-lint-tools" = [
                pkgs.lychee
              ];
            };
          };
        };
    };
}
