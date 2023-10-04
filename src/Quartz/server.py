"""This is the server module"""

try:
    from Quartz import IPTYPE
except ModuleNotFoundError:
    import os, sys

    dir_path = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(f"{dir_path}/..")
    pass

from Common import *
from ServerLib import *
import atexit
from typing import Callable


def main() -> None:
    """This is Servers main function"""

    server = serverClass.Server()

    # These are the lists needed for threads creation
    managerList: list[Callable] = [
        serverManagers.ConnectionsManager,
        serverManagers.ChatManager,
        serverManagers.ServerInputManager,
    ]
    managerList.extend(server.PluginManagers())

    argumentsList = [server]

    # This will be executed whenever the server ends
    atexit.register(serverWire.CloseServer, connections=server.connections, s=server.s)

    # Threads creation and join
    threadsList = threads.ThreadSetup(managerList, argumentsList)
    for thread in threadsList:
        thread.join()


if __name__ == "__main__":
    main()
