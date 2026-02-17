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
        {
          devshells.default = {
            commandGroups = {
              docs = [
                {
                  name = "find-broken-links";
                  command = "${pkgs.lib.getExe pkgs.markdown-link-check} -i .venv -i .git -q .";
                  help = "Find all broken links in all Markdown files";
                }
              ];
            };
          };
        };
    };
}
