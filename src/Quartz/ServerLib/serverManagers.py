'''This module stores all core Server Managers'''

from ServerLib import serverWire
from ServerLib import serverClass
from time import sleep

# This Manager accept new connections
def ConnectionsManager(server: serverClass.Server) -> None:
   """This function manages all incoming connections from clients and was built to be a thread target"""
   
   while True:
      sleep(0.2)
      
      serverWire.AcceptConnections(server.connections, server.s)

# This Manager receives messages and send messages 
def ChatManager(server: serverClass.Server) -> None:
   """This function manages chat, receiving and sending messages, was built to be a thread target"""

   while True: 
    sleep(0.2)
    messageList = serverWire.ReceiveMessage(server.connections)

    for message in messageList:
        if message != None:
            if message.text != None: # If the connection with someone has ended, this will be evaluated as none
               possibleCommand = message.text.lower().split()[0]

               # Built in Commands
               if (possibleCommand == "/username") and (len(message.text.split()) > 1):
                  server.changeUsername(message)
               
               # Plugin Commands
               elif (server.CheckCActions(message.text, possibleCommand, message) == True):
                  continue
         
               else:
                  message.username = server.usernames[server.connections.index(message.sender)]
                  serverWire.SendMessage(server.connections,message)


            else:
                server.removeUser(message)

def ServerInputManager(server: serverClass.Server) -> None:
   """This function manages all input commands from server"""
   while True:
      message = input()
      server.CheckSActions(message, message.lower().split()[0])