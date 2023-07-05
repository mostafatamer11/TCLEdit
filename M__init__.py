from time import sleep
from sys import stdout
import sys
import signal

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
    OKBLUE = '\033[94m'
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
    UNBOLD = "\033[22m"
    UNUNDERLINE = "\033[24m"



    def cursor(movement:str, times:int):
        print(f"\033[{times}{movement}")


    def __error(self):
        print("CTAEditError: You didnt assign a vlaue for fg or bg")
        return


    def rgb(self, **kwargs):
        # This 2 lines statement checks if you typed the correct parameters its advanced py and its not
        # nesserly a skill                                                                            the backslash divides the code into two lines
        assert (("fg" in kwargs) and (type(kwargs.get("fg", None) == tuple) and (len(kwargs.get("fg", "0")) == 3)))\
            or (("bg" in kwargs) and (type(kwargs.get("bg", None) == tuple) and (len(kwargs.get("bg", "0")) == 3)))\
                , "YOU DIDN'T WRITE 'fg=(r, g, b)' or 'bg=(r, g, b)'"

        r1, g1, b1 = kwargs.get("fg", (TypeError(self.__error), TypeError(self.__error), TypeError(self.__error)))
        r2, g2, b2 = kwargs.get("bg", (TypeError(self.__error), TypeError(self.__error), TypeError(self.__error)))
        print(f"\033[38;2;{r1};{g1};{b1}m")
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
        print(CTAEdit.rgb(args))

    for char in word:
        print(char, end="")
        stdout.flush()
        sleep(time)
    print("\n")

    print(CTAEdit.ENDC)

def signal_handler(signum, frame):
    # This will run when the signal is recieved
    print(CTAEdit.ENDC)
    # Clean up nicely then exit
    sys.exit(0)

# Register signal_handler with SIGINT
signal.signal(signal.SIGINT, signal_handler)
#hi mostafa 

