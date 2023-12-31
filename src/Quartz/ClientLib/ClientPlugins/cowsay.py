"""
This Plugin is just an example of a command plugin, as this is a client plugin, it should be placed at ClientLib/ClientPlugins
"""
import os
from Common.messageLib import Msg  # type: ignore


def commands(
    client, message: str, possibleCommand: str, role: str, msgObject: Msg
) -> bool:
    if possibleCommand == "/cowsay":
        message = str(message.split(" ", 1)[1])


        if role == "receiver":
            print(msgObject)
            os.system(f"cowsay {message}")
            return True

        else:
            os.system(f"cowsay {message}")
            return False
    return False
