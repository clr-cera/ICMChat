"""This module stores all server's network functions"""

import socket
from Common import messageLib as msgl
from Quartz import IPTYPE


# Create the server socket
def CreateServerSocket(host: str, port: int) -> socket.socket:
    """This function creates the server socket and binds to host and port"""

    if IPTYPE == "IPV6":
        s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
        s.bind((host, port, 0, 0))
    else:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        s.bind((host, port))

    s.listen(50)
    s.setblocking(False)

    return s


# Sends the message to all connections
def SendMessage(connections: list[socket.socket], message: msgl.Msg) -> None:
    """This function sends a message to all connections except the sender"""

    print(str(message))

    for c in connections:
        if c != message.sender:
            c.sendall(message.encode())


def SendServerMessage(connections: list[socket.socket], message: msgl.Msg) -> None:
    """This function sends a message as the server"""

    message.setServerMessage()
    SendMessage(connections, message)


# Receive messages from all connections and checks if any connection has been broken, returns a list of Msg objects with the message and sender, if the connection is broken, the sender is None. If there is no message, returns None
def ReceiveMessage(connections: list[socket.socket]) -> list[msgl.Msg]:
    """Receive messages from all connections and checks if any connection has been broken, returns a list of Msg objects with the message and sender.
    \n If the connection is broken, the text is None.
    \n If there is no message, returns None."""

    messagesList: list[msgl.Msg] = []

    if len(connections) > 0:
        # print(len(connections)) #DEBUG

        for c in connections:
            try:
                message = c.recv(4096)

                if message:
                    try:
                        messagesList.append(msgl.Msg.decode(message))

                    except:
                        print("Message is not being decoded!")
                        continue

                    messagesList[-1].setSender(c)

                else:
                    messagesList.append(msgl.Msg(None, c))

            except:
                pass

    return messagesList


# Accepts any new connections
def AcceptConnections(connections: list[socket.socket], s: socket.socket) -> None:
    """This function accepts new connections and append them to connections list"""

    try:
        c, addr = s.accept()  # Establish connection with client.
        c.setblocking(False)
        connections.append(c)
        print(f"accepted connection from {c}")
    except:
        pass


def CloseServer(connections: list[socket.socket], s: socket.socket) -> None:
    """This function closes all connections, the socket of the server and clear connections list"""

    for c in connections:
        c.close()
    s.close()

    connections.clear()
    print("All connections were ended!")
