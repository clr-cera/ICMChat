'''This module defines the server class and the dictionary of all server plugins'''

from ServerLib import serverWire
from socket import socket
from Common import *

from types import ModuleType
import importlib
import pkgutil
from ServerLib import ServerPlugins
from Common.messageLib import Msg
from typing import Any, Dict, Callable


def iter_namespace(ns_pkg):
    # Specifying the second argument (prefix) to iter_modules makes the
    # returned name an absolute name instead of a relative one. This allows
    # import_module to work without having to do additional modification to
    # the name.
    return pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + ".")

discovered_plugins = [
    importlib.import_module(name)
    for finder, name, ispkg
    in iter_namespace(ServerPlugins)
]

class Server:
    '''This class manages all data and main methods the server needs to'''

    def __init__(self) -> None:
        self.connections: list[socket]= []
        self.usernames: list[str]= []
        self.s: socket= serverWire.CreateServerSocket(serverData.HOST, serverData.PORT)
        self.plugins: list[ModuleType]= discovered_plugins
        self.data: Dict[str, Any]= []

        for plugin in self.plugins:
            print(plugin.__name__)

    def removeUser(self, message: messageLib.Msg) -> None:
        '''This function removes user from connections and usernames lists'''

        try:
            userIndex = self.connections.index(message.sender)
            message.username = self.usernames[userIndex]

            self.usernames.pop(userIndex)
            self.connections.pop(userIndex)

            message.text = f"{message.username} has left the chat."
            message.isServer = True
            serverWire.SendServerMessage(self.connections,message)

        except:
            self.connections.pop(userIndex)

    # This function changes or inserts a username in the usernames list
    def changeUsername(self, message: messageLib.Msg) -> None:
        '''This function changes or inserts the username of an user in the username list'''

        newUsername = message.text.split()[1]

        try:
            oldEntry = self.usernames[self.connections.index(message.sender)]
            self.usernames[self.connections.index(message.sender)] = newUsername

            if oldEntry == None:
                message.text = f"{newUsername} has entered the chat."
                serverWire.SendServerMessage(self.connections,message)

            else:
                message.text = f"{oldEntry} has changed their name to {newUsername}"
                serverWire.SendServerMessage(self.connections,message)
        
        

        except:
            difference = self.connections.index(message.sender)+1 - len(self.usernames)
            self.usernames.extend([None]*difference)

            self.usernames[self.connections.index(message.sender)] = newUsername

            message.username = newUsername
            message.text = f"{message.username} has entered the chat."

            serverWire.SendServerMessage(self.connections,message)

    def CheckCActions(self, message: str, possibleCommand: str, msgObject: Msg) ->None:
        '''This Function iterates on all plugins searching for client commands to check'''
        for plugin in self.plugins:
            try:
                if plugin.clientCommands(self, message, possibleCommand, msgObject) == True:
                    return True
            except:
                pass
        return False

    def CheckSActions(self, message: str, possibleCommand: str) ->None:
        '''This Function iterates on all plugins searching for server commands to check'''
        for plugin in self.plugins:
            try:
                if plugin.serverCommands(self, message, possibleCommand) == True:
                    return True
            except:
                pass
        return False
    
    def PluginManagers(self) -> list[Callable]:
        '''This Function iterates on all plugins searching for managers'''
        pluginManagerList = []

        if len(self.plugins) > 0:
            for plugin in self.plugins:
                try:
                    pluginManagerList.extend(plugin.MANAGERLIST)
                except:
                    pass
                    
        return pluginManagerList