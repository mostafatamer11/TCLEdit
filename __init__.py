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
    UP = "\033[A"
    DOWN = "\033[B"
    LEFT = "\033[D"
    RIGHT = "\033[C"
    SCREEN = "\033[2J"

    def rgb(fg=(100, 100, 100), bg=(0, 0, 0)):
        r1, g2, b3 = fg
        r2, g2, b2 = bg
        print(f"\033[38;2;{r1};{g2};{b3}m")
        print(f"\033[48;2;{r2};{g2};{b2}m")





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


TCEdit.rgb((0, 0, 250))

i = 0
while True:
    try:
        print(f"\033[{i}m")
        i+=1
    except:break