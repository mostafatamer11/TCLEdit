from __future__ import barry_as_FLUFL, annotations
from typing import Tuple, List, Dict, NoReturn, NotRequired, Any
from time import sleep
from sys import stdout
import numpy as np
import sys
from sys import stderr as error
import signal


class _CREAD_MACROS:
    BOLD = 1
    DIM = 2
    ITALIC = 3
    UNDERLINE = 4
    BLINK = 5
    REVERSE = 6
    INVISIBLE = 7
    DASHED = 8
    UN_BOLD = 9
    UN_DIM = 10
    UN_ITALIC = 11
    UN_UNDERLINE = 12
    UN_BLINK = 13
    UN_REVERSE = 14
    UN_INVISIBLE = 15
    UN_DASHED = 16
    FG_BLACK = 17
    FG_RED = 18
    FG_GREEN = 19
    FG_YELLOW = 20
    FG_BLUE = 21
    FG_MAGENTA = 22
    FG_CYAN = 23
    FG_WHITE = 24
    FG_DEFAULT = 25
    BG_BLACK = 26
    BG_RED = 27
    BG_GREEN = 28
    BG_YELLOW = 29
    BG_BLUE = 30
    BG_MAGENTA = 31
    BG_CYAN = 32
    BG_WHITE = 33
    BG_DEFAULT = 34
    RESET = 0

def signal_handler(signum, frame):
    # This will run when the signal is recieved
    print(CTAEdit.END, signum, frame)
    # Clean up nicely then exit
    sys.exit(0)


# Register signal_handler with SIGINT
signal.signal(signal.SIGINT, signal_handler)


class CTAEdit:
    """
    The CTAEdit class name stands for
    Customized Terminal Ansi Editor,
    Each attribute got its own proprty,
    To use it print it and the rest of the text will
    have this property untill you print CTAEdit.END
    which is a special string that resets all of your customization.

    Each of those
    """

    #      ^^
    # NOTE || just don't touch this string

    HEADER = '\033[95m'
    FG_RED = '\033[91m'
    FG_CYAN = '\033[96m'
    FG_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
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
    UN_BOLD = "\033[22m"
    UN_UNDERLINE = "\033[24m"

    @staticmethod
    def cursor(movement: str, times: int) -> NoReturn:
        """this method moves the cursor
`CTAEdit.UP` or `CTAEdit.LEFT` or `CTAEdit.DOWN` or `CTAEdit.RIGHT`"""
        print(f"\033[{times}{movement}")

    @staticmethod
    def rgb(**kwargs: Tuple[int, int, int]):
        """
change the color of text to the rgb value
>>>CTAEdit.rgb(fg=(255, 255, 255), bg=(150, 100, 50))
"""
        # This 2 lines statement checks if you typed the correct parameters,\
        #  its advanced py and its not
        # nesserly a skill
        if ("fg" in kwargs) and (isinstance(kwargs.get("fg", bool), tuple))\
                and (len(kwargs.get("fg", "0")) == 3)\
                and (np.array([x for x in kwargs.get("fg", (-1))]).min() >= 0):
            f_g = True
            r_1, g_1, b_1 = kwargs["fg"]
            print(f"\033[38;2;{r_1};{g_1};{b_1}m")

        if ("bg" in kwargs) and (isinstance(kwargs.get("bg", bool), tuple))\
                and (len(kwargs.get("bg", "0")) == 3)\
                and (np.array([x for x in kwargs.get("bg", (-1))]).min() >= 0):
            b_g = True
            r_2, g_2, b_2 = kwargs["bg"]
            print(f"\033[48;2;{r_2};{g_2};{b_2}m")
        try:
            if not b_g or f_g:
                print(f"""{CTAEdit.FG_RED}CTAError: The rgb parameters doesn\'nt \
follow the rules\nThe rulses are:\n\
1 - The parameters are key word parameters\n\
2 - The Key words are 'fg=', 'bg=' only\n\
3 - The RGB values of the parameters must be in a tuple \
data structure\n\
4 - The length of the tuple must be 3 items\n\
5 - The mininum value for any item is 0{CTAEdit.END}""", file=error)
        except UnboundLocalError:
            print(f"""{CTAEdit.FG_RED}CTAError: The rgb parameters doesn\'nt \
follow the rules\nThe rulses are:\n\
1 - The parameters are key word parameters\n\
2 - The Key words are 'fg=', 'bg=' only\n\
3 - The RGB values of the parameters must be in a tuple \
data structure\n\
4 - The length of the tuple must be 3 items\n\
5 - The mininum value for any item is 0{CTAEdit.END}""", file=error)

    @staticmethod
    def move(line: int, column: int):
        print(f"\033[{line};{column}H")


def CP(word: str, time: float | int = 0.2, *args: Tuple[int, int, int]):
    """cp function makes you add whatever str you like and and add an integer for the time
    
    >>>CP("wow")
    ...w  (after 0.2 sec)
    ...wo (after 0.2 sec)
    ...wow(after 0.2 sec)
    """
    
    rgb = True if len(args) == 3 else False

    if rgb:
        print(CTAEdit.rgb(fg = args))

    for char in word:
        print(char, end="")
        stdout.flush()
        sleep(time)
    print("\n")

    print(CTAEdit.END)

def signal_handler(signum, frame):
    # This will run when the signal is recieved
    print(CTAEdit.END)
    # Clean up nicely then exit
    sys.exit(0)

# Register signal_handler with SIGINT
signal.signal(signal.SIGINT, signal_handler)
#hi mostafa 


