# if you have nix you can use this as a shell without having to install python and gcc

{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell
{
  nativeBuildInputs = with pkgs; [
    python3
    libgcc 
  ];
}
