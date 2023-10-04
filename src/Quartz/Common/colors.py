"""This module eases color use"""

COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "lightPurple": "\033[94m",
    "purple": "\033[95m",
    "cyan": "\033[96m",
    "lightGray": "\033[97m",
    "black": "\033[98m",
}
RESETCOLOR = "\033[00m"


def __printColors(color: str):
    if color == "exit":
        exit()
    if color in COLORS:
        print(f"{COLORS[color]}I liked this color!{RESETCOLOR}\n")
    else:
        print("I dont understand this color!\n")


def __main():
    while True:
        color = input("Type your desired color:\n")
        __printColors(color)


if __name__ == "__main__":
    __main()
