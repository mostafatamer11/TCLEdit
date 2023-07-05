from time import sleep
from sys import stdout
import sys
import signal

class TCAEdit:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    DOWN = "B"
    LEFT = "D"
    RIGHT = "C"
    UP = "A"
    SCREENCLEAR = "\033[2J"
    WHITE = "\033[97m"
    LINEUP = "\033[2A"
    LINECLEAR = "\033[2K"
    HOME = "\033[H"
    INVISIBLE = "\033[?25l"
    VISIBLE = "\033[?25h"


    def cursor(movement:str, times:int):
        print(f"\033[{times}{movement}")


    def rgb(fg=(100, 100, 100), bg=(0, 0, 0)):
        r1, g2, b3 = fg
        r2, g2, b2 = bg
        print(f"\033[38;2;{r1};{g2};{b3}m")
        print(f"\033[48;2;{r2};{g2};{b2}m")


    def move(line:int, column:int):
        print(f"\033[{line};{column}H")


def CP(word:str, time:float|int = 0.2, *args):
    """cp function makes you add whatever str you like and and add an integer for the time
    
    >>>CP("wow")
    ...w  (after 0.2 sec)
    ...wo (after 0.2 sec)
    ...wow(after 0.2 sec)
    """
    
    rgb = True if len(args) == 3 else False

    if rgb:
        print(TCAEdit.rgb(args))

    for char in word:
        print(char, end="")
        stdout.flush()
        sleep(time)
    print("\n")

    print(TCAEdit.ENDC)

def signal_handler(signum, frame):
    # This will run when the signal is recieved
    print(TCAEdit.ENDC)
    # Clean up nicely then exit
    sys.exit(0)

# Register signal_handler with SIGINT
signal.signal(signal.SIGINT, signal_handler)
