{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    devshell.url = "github:deemp/devshell";
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
            commandGroups = {
              lint = [
                {
                  name = "find-broken-links";
                  command = ''
                    ${pkgs.lib.getExe pkgs.lychee} \
                      --include-fragments \
                      --offline \
                      --no-progress \
                      --exclude-path '.venv' \
                      --exclude-path '.direnv' \
                      --root-dir . \
                      --cache \
                      --format json \
                      '**/*.md' \
                      | ${pkgs.lib.getExe python} lab/design/scripts/lychee-locate.py
                  '';
                  help = "Find all broken links in all Markdown files (with file:line locations)";
                }
                {
                  name = "lint-docs";
                  command = ''
                    ${pkgs.lib.getExe pkgs.markdownlint-cli2} \
                      '**/*.md' '#.direnv' '#.venv'
                  '';
                  help = "Lint all Markdown files";
                }
              ];
              tools = [
                pkgs.lychee
              ];
            };
          };
        };
    };
}
