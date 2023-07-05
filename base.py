import numpy as np

BASE = {16: ({indx: char for indx, char in enumerate("0123456789abcdef")})}
BASES = {char: str(indx) for indx, char in enumerate("0123456789abcdef")}

# base = 16
# print([(lambda x: base ** x)(x) for x in range(2, -1, -1)])


def conv(num, base):
    formula = np.array([])

    for indx, char in enumerate(num):
        formula = np.append(formula, int(BASES[char]) * (base ** indx))
    
    formula = formula.sum()



    return(formula)


def to_base(number:str, base=10):
    num = ""
    for no in number:
        num += BASES[16][no]
    int(num, base=16)
    r = 0
    q = num
    result = str()

    while q:
        r = q%base
        q = q//base
        result += (BASES[16][r])

    result = result[::-1]
    return (result)


