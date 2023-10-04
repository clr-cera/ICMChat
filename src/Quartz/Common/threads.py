from threading import Thread
from typing import Callable, Any


def ThreadSetup(managerList: list[Callable], argumentsList: list[Any]) -> list[Thread]:
    """This functions takes a list of managers,
    a list of arguments and initializes all managers as separated threads,
    it returns a list with all threads"""

    threadsList = []
    for manager in managerList:
        t = Thread(target=manager, args=argumentsList, daemon=True)
        t.start()
        threadsList.append(t)

    return threadsList
