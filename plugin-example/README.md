## Plugin Creation
### Client Plugin
Every Client Plugin will be scaned for one function and a list.
- commands()
The first function is commands(), this is the necessary header of any commands function:
```python
(function) def commands(
client,
message: str,
possibleCommand: str,
role: str,
msgObject: Msg
) -> bool
```
This function receives the client object (See src/Quartz/ClientLib/clientClass.py for client class), a string message, a string possible command, the role(If it is a receiver or the sender of given message) and a Msg object (See src/Quartz/common/messageLib for Msg class). This function is called everytime the client sends or receives a message, if it returns False, the message will continue to be passed to other commands(), and in the end, it will be printed if receiver or sent to server if sender. If a plugin's commands() wants for that message to not be printed or sent, it should return True if given role. See cowsay.py for an example of Client Plugin with commands() function.

- MANAGERLIST
The list is MANAGERLIST, this list should contain functions with this header:
```python
(function) def manager(
client,
) -> None
```
This function receives the client object (See src/Quartz/ClientLib/clientClass.py for client class). All function inside MANAGERLIST are going to be the target of newly created threads on client initialization. The plugin creator will be responsible to all these threads operations and its end, the client has a method CheckState() that can be used to end the thread when the user wants to quit.

### Server Plugin
Every Server Plugin will be scaned for two functions and one list.
- clientCommands()
The first function is clientCommands(), this is the necessary header of any clientCommands function:
```python
(function) def clientCommands(
server,
message: str,
possibleCommand: str,
msgObject: Msg
) -> bool
```
This function receives the server object (See src/Quartz/ServerLib/serverClass.py for server class), a string message, a string possible command and a Msg object (See src/Quartz/common/messageLib for Msg class). This function is called everytime the server receives a message, if it returns False, the message will continue to be passed to other clientCommands(), and in the end, it will be sent to all connections except receiver. If a plugin's clientCommands() wants for that message to not be sent to all connections, it should return True.

- serverCommands()
The second function is serverCommands(), this is the necessary header of any serverCommands function:
```python
(function) def serverCommands(
server,
message: str,
possibleCommand: str,
) -> bool
```
This function receives the server object (See src/Quartz/ServerLib/serverClass.py for server class), a string message and a string possible command. This function is called everytime the server gives an input to the terminal, if it returns False, the message will continue to be passed to other serverCommands().
- MANAGERLIST
The list is MANAGERLIST, this list should contain functions with this header:
```python
(function) def manager(
server,
) -> None
```
This function receives the server object (See src/Quartz/ServerLib/serverClass.py for server class). All function inside MANAGERLIST are going to be the target of newly created threads on server initialization. The plugin creator will be responsible to all these threads operations.
