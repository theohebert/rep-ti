let
  rev = "";     # choose a nixpkgs commit (e.g., from the stable 24.05 branch)
  sha256 = "";  # a safety checksum; Nix tells you the right value on first run
in
import (builtins.fetchTarball {
  url = "https://github.com/NixOS/nixpkgs/archive/${rev}.tar.gz";
  inherit sha256;
})

