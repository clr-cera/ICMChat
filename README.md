# Quartz
Quartz is an extensible tcp chat. It provides a server and a client with more than enough flexibity to suit your use case. It can be deployed in a local network or in the internet with ease due to `nix` integration. To create a Quartz based chat, one can fork this repo and make little changes as described in the Configuration section.

## About
- Authors: clr-cera
- License: MIT License
- Download: https://codeload.github.com/clr-cera/Quartz/zip/refs/heads/main
- Bug reports: https://github.com/clr-cera/Quartz/issues
- git clone https://github.com/clr-cera/Quartz.git
  
## Design Goals
- An easily and completely extensible tcp chat in python
- An easy, fast and integrated deployment using nix
- Console-based but web extensible as well

## Features
- Tcp basic console chat
- Plugin system
- Commands interface
- User selected names and colors

## Dependencies
### Obligatory Dependencies
- `Python` for everything
- `dnspython` for domain resolving
### Optional Dependencies
- `nix` for installation and deployment
- `docker`  for nix produced docker use

## Installing Client
This repo has a Quartz package available inside the flake and also can be installed via `pip`.
### Pip installation: 
```
pip install .
```

### Nix run:
```
nix run github:OWNER/CHAT_REPO
```
This command will "install" everything and run the client automatically.

### In a Nixos flake system:
In flake.nix:
```nix
{
  # create an input with the name of the chat, and set its url to this repository
  inputs.CHATNAME.url = github:OWNER/CHATREPO;
}
```
In configuration.nix:
```nix
{
environment.systemPackages = [inputs.CHATNAME.packages.YOUR_SYSTEM.default];
}
```
## Configuration
### If you want to add plugins to a Quartz based client:
Plugins for client can be inserted in ~/.config/chatname/plugins/.

This folder is automatically created on first client execution.
### If you want to configure a Quartz based chat, you can follow these steps:
0. Step Zero: Fork it, if you are going to make a Quartz based chat please do not send any configuration commit to this repo.
  
1. Firstly: You can find and replace Quartz for whatever name you want inside flake.nix and change the name and console_scripts name inside setup.cfg. Please dont replace the name inside Src!!! (It can break!)
 
2. Secondly: You can enter your information in src/Quartz/__init__.py, such as chat's name, domain, ip, iptype(IPV6 or IPV4) and version. Here, if given IP it will be used, if not, the domain will be converted as IP and if no domain nor IP is given, the host will be localhost.
  
3. Thirdly: You can put every plugin you want inside their respective directories. For Client PLugins: src/Quartz/Clientlib/ClientPlugins. For Server Plugins: src/Quartz/ServerLib/ServerPlugins. Every plugin inserted will be automatically capted by client and Server.

4. Deploy it with your desired method and publish the client!

## Deploy
The server can be deployed in various ways:
- Nix run
```
nix run .#Server
```
This command will install all dependencies and run the server.
- Docker
  
The flake inside this repo makes a docker image available so one can enter:
```
nix build .#Docker
```
In the working directory a `result` docker image with all dependencies will be created. Inside it the `CHATNAME-Server` command can be used to start the server.
- Directly

if one wants, they can just run: 
```
python src/Quartz/server.py
```
Everything should be up and running if all obligatory dependencies are met.

## Plugin Creation
See [plugins instructions](./plugin-example/README.md).

### Credits
Ranger file manager's README was a heavy inspiration for this file and I am very thankful.
