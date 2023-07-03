from time import sleep
from sys import stdout



class TCEdit:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def rgb(rgb):
        r, g, b = rgb
        return f"\u001b[38;2;{r};{g};{b}m"



def CP(word:str, time:float|int = 0.2, *args):
    """cp function makes you add whatever str you like and and add an integer for the time
    
    >>>CP("w0w")
    ...w  (after 0.2 sec)
    ...wo (after 0.2 sec)
    ...wow(after 0.2 sec)
    """
    
    rgb = True if len(args) == 3 else False

    if rgb:
        print(TCEdit.rgb(args))

    for char in word:
        print(char, end="")
        stdout.flush()
        sleep(time)
    print("\n")

    print(TCEdit.ENDC)
