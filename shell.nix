{pkgs ? import <nixpkgs> {}}: let
  pythonEnv = pkgs.python3.withPackages (ps: with ps; [dnspython build black ]);
in
  (pkgs.buildFHSUserEnv {
    name = "pip-Install-Shell";
    targetPkgs = pkgs: [
      pythonEnv
      pkgs.python3Packages.pip
      pkgs.python3Packages.virtualenv
    ];
    runScript = "bash";
  })
  .env
