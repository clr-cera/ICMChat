'''This is the client module'''

try:
   from Quartz import IPTYPE, NAME
except ModuleNotFoundError:
   import os, sys
   dir_path = os.path.dirname(os.path.realpath(__file__))
   sys.path.append(f"{dir_path}/..")
   pass

import os, sys
CONFDIR = os.path.expanduser(f'~/.config/{NAME.lower()}')
sys.path.append(CONFDIR)

from ClientLib import *
from ClientLib.clientManagers import *
from Common import *
from typing import Callable


def ConfigSetup(configpath):
   if (os.path.exists(f"{configpath}")):
      if (os.path.exists(f"{configpath}/plugins")):
         if os.path.exists(f"{configpath}/plugins/__init__.py"):
            return
           
         else:   
            f = open(f"{configpath}/plugins/__init__.py", "w")
            f.close()
      
      else: os.mkdir(f"{configpath}/plugins")
   else: os.mkdir(configpath)
   
   ConfigSetup(configpath)
ConfigSetup(CONFDIR)


def main() -> None:
   '''This is clients main Function'''

   clientInterface.clearScreen()
   # This is an object that will be used to track the clients current state and carry main properties
   client = clientClass.Client()

   # This Starts the Interface
   clientInterface.InterfaceStart(client)

   # These are all necessary parameters for the creation of threads
   managerList: list[Callable]= [ReceiveManager, SendManager]
   managerList.extend(client.PluginManagers())

   argumentsList = [client]

   # This creates all necessary threads
   threadsList = threads.ThreadSetup(managerList, argumentsList)
   client.threads = threadsList

   for thread in threadsList:
      thread.join()





if __name__ =="__main__":
   main()
