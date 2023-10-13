"""This module stores every little complex interface functions"""

from time import sleep
from ClientLib import clientClass, clientWire
from Common import messageLib as mlib, colors
from Quartz import NAME
import os, sys


def InterfaceStart(client: clientClass.Client) -> None:
    """This function receives initial info from user"""

    clearScreen()
    print(f"Welcome to {NAME}!")
    sleep(1)

    ReceiveUsername(client)
    ReceiveColor(client)

    print("--------------Chat--------------")

    clientWire.sendCMessage(
        client.s,
        mlib.Msg(text=f"/username {client.username}", username=client.username),
    )


def MessageInput(client: clientClass.Client) -> str:
    try:
        return input()  # UserInput(client)

    except:
        client.shutdown()


def ReceiveUsername(client: clientClass.Client) -> None:
    """This function receives username from user"""

    username = input("Type your username:\n")
    printSent(f"Your username will be {username.split()[0]}!")
    client.setUsername(username.split()[0])
    sleep(1)
    print("If you desire to change it later on, you can enter /username USERNAME")


def ReceiveColor(client: clientClass.Client) -> None:
    """This function receives color from user"""

    while True:
        color = input(
            f"""Select a Color!
{colors.COLORS['red']}red 
{colors.COLORS['green']}green    
{colors.COLORS['yellow']}yellow 
{colors.COLORS['lightPurple']}lightPurple 
{colors.COLORS['purple']}purple 
{colors.COLORS['cyan']}cyan 
{colors.COLORS['lightGray']}lightGray 
{colors.COLORS['black']}black
{colors.RESETCOLOR}"""
        )

        if color in colors.COLORS:
            printSent(
                f"Your color will be {colors.COLORS[color]}{color}{colors.RESETCOLOR}!"
            )
            client.setColor(color)
            break

        else:
            printSent("Your selected color is not available!")

    sleep(1)
    print("If you desire to change it later on, you can enter /color")


def clearScreen() -> None:
    os.system("clear")


def printSent(string: str) -> None:
    print(string)
    """
    print("\033[F"+string)
    """


def printIncoming(string: str, client: clientClass.Client) -> None:
    print(string)
    """print("\n",end="")
    print("\033[1A\033[1L",end="")
    print(string,end="\n")
    if client.cursorColumn != 0:
        os.system(f"tput cuf {client.cursorColumn}")"""


"""def UserInput(client: clientClass.Client) -> str:
    string: str= ""
    char: str= sys.stdin.read(1)
    while char != '\n':
        client.cursorColumn += 1
        string = string + char
        char = sys.stdin.read(1)

    client.cursorColumn = 0
    return string"""
