"""This module defines the client class and the dictionary of all client plugins"""

from threading import Thread
from socket import socket

from ClientLib import clientWire, ClientPlugins, clientInterface
from Common import serverData, colors
from Common.messageLib import Msg
import plugins  # type: ignore

from types import ModuleType
import importlib
import pkgutil
from typing import Any, Dict, Callable


def iter_namespace(ns_pkg):
    # Specifying the second argument (prefix) to iter_modules makes the
    # returned name an absolute name instead of a relative one. This allows
    # import_module to work without having to do additional modification to
    # the name.
    return pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + ".")


discovered_plugins = [
    importlib.import_module(name)
    for finder, name, ispkg in iter_namespace(ClientPlugins)
] + [importlib.import_module(name) for finder, name, ispkg in iter_namespace(plugins)]


class Client:
    """This class manages all data and main methods the client needs to"""

    def __init__(self, state: str = "ON"):
        self.state: str = state
        self.username: str = None
        self.color: str = None
        self.threads: list[Thread] = None
        self.plugins: list[ModuleType] = discovered_plugins
        self.data: Dict[str:Any] = {}
        self.cursorColumn: int = 0

        # The socket is automatically connected when Client is innitialized
        self.s: socket = clientWire.connectSocket(serverData.HOST, serverData.PORT)

    def shutdown(self) -> None:
        self.state = "SHUTDOWN"
        exit()

    def setUsername(self, name: str) -> None:
        self.username = name

    def setColor(self, color: str) -> None:
        if color in colors.COLORS:
            self.color = color
        else:
            print("The color you have chosen is not available")

    def CheckState(self) -> None:
        """This function checks the client state and takes an action if necessary"""
        if self.state == "SHUTDOWN":
            exit()

    def CheckActions(
        self, message: str, possibleCommand: str, role: str, msgObject: Msg
    ) -> None:
        """This Function iterates on all plugins searching for commands to check, role can be "sender" or "receiver", which will be defined by the manager"""
        for plugin in self.plugins:
            try:
                if (
                    plugin.commands(self, message, possibleCommand, role, msgObject)
                    == True
                ):
                    return True
            except:
                pass
        return False

    def PluginManagers(self) -> list[Callable]:
        """This Function iterates on all plugins searching for managers"""
        pluginManagerList = []

        if len(self.plugins) > 0:
            for plugin in self.plugins:
                try:
                    pluginManagerList.extend(plugin.MANAGERLIST)
                except:
                    pass

        return pluginManagerList
