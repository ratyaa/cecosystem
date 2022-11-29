{ pkgs ? import <nixpkgs> {} }:

let
  python = pkgs.python39;
  pypackage = pkgs.python39Packages;
  
  pythonPackages = python.buildEnv.override {
    extraLibs = [
      pypackage.numpy
      pypackage.matplotlib
      pypackage.pygame
    ];
  };
in
      
pkgs.mkShell {
  buildInputs = [
    pythonPackages
    pkgs.plantuml
  ];
}
