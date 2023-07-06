from __future__ import barry_as_FLUFL, annotations
from typing import Tuple, List, Dict, NoReturn, NotRequired, Any
from time import sleep
from sys import stdout
import numpy as np
import sys
from sys import stderr as error
import signal


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
    def cursor(movement:str, times:int) -> NoReturn:
        print(f"\033[{times}{movement}")


    def rgb( **kwargs: Tuple[int, int, int]):
        """You are right"""
        # This 2 lines statement checks if you typed the correct parameters,\
        #  its advanced py and its not
        # nesserly a skill
        if not (("fg" in kwargs) and (isinstance(kwargs.get("fg", None)), tuple)\
                and (len(kwargs.get("fg", "0")) == 3) and (np.array([x for x in kwargs.get("fg", (-1))]).min() >= 0))\
            or (("bg" in kwargs) and (type(kwargs.get("bg", None)) == tuple)\
                and (len(kwargs.get("bg", "0")) == 3) and (np.array([int(x) for x in kwargs.get("bg", (-1))]).min() >= 0))\
                :
                print(f"{CTAEdit.FG_RED}CTAError: The rgb parameters doesn\'nt follow the rules\nThe rulses are:\n\
                        1 - The parameters are key word parameters\n\
                        2 - The Key words are 'fg=', 'bg=' only\n\
                        3 - The RGB values of the parameters must be in a tuple data structure\n\
                        4 - The length of the tuple must be 3 items\n\
                        5 - The mininum value for any item is 0{CTAEdit.END}", file=error)

        r1 = g1 = b1 = None
        if kwargs.get("fg", None):
            r1, g1, b1 = kwargs.get("fg") 
        if kwargs.get("bg", None):
            r2, g2, b2 = kwargs.get("bg") 

        if kwargs.get("fg", None):
            print(f"\033[38;2;{r1};{g1};{b1}m")

        if kwargs.get("bg", None):
            print(f"\033[48;2;{r2};{g2};{b2}m")


    def move(line:int, column:int):
        print(f"\033[{line};{column}H")


def CP(word:str, time:float|int = 0.2, *args: Tuple[int, int, int]):
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


CTAEdit.rgb(fg = (1, 1, 1))