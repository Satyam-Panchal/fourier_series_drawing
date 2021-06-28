# tuple to complex number convertor (tuple size muist be even since for set of *points* which require 2 stuff
tc = lambda t: list((complex(t[x], t[x + 1]) for x in range(0, len(t), 2)))


# Gets the stuff between 2 alphabets in form of tuple (or single number if H or V)
def getNum(string, index):
    # returns tuple
    x = ''
    while True:
        if string[index].isalpha(): break
        x += string[index]
        index += 1
    return eval(x), index


# the good stuff, brings everything together. Input is the weirdo string, output is the weirdo list of list of complex number points
def goodData(data):
    FINAL = []
    dat = []
    x = 1
    pp1, x = getNum(data, x)
    pp2 = 0
    while True:
        if data[x] == "C":
            x += 1
            ls = getNum(data, x)
            x = ls[1]
            dat = pp1 + ls[0]
            pp2 = dat[-4:-2]
            pp1 = dat[-2:]
            FINAL.append(tc(dat))
        elif data[x] == 'S':
            x += 1
            ls = getNum(data, x)
            x = ls[1]
            dat = pp1 + (2 * pp1[0] - pp2[0], 2 * pp1[1] - pp2[1]) + ls[0]
            pp2 = dat[-4:-2]
            pp1 = dat[-2:]
            FINAL.append(tc(dat))
        elif data[x] == 'H':
            x += 1
            ls = getNum(data, x)
            x = ls[1]
            dat = pp1 + (ls[0], pp1[1])
            pp1 = dat[-2:]
            FINAL.append(tc(dat))
        elif data[x] == 'V':
            x += 1
            ls = getNum(data, x)
            x = ls[1]
            dat = pp1 + (pp1[0], ls[0])
            pp1 = dat[-2:]
            FINAL.append(tc(dat))
        elif data[x] == 'L':
            x += 1
            ls = getNum(data, x)
            x = ls[1]
            dat = pp1 + ls[0]
            pp1 = dat[-2:]
            FINAL.append(tc(dat))
        elif data[x] == 'Z':
            break
    return FINAL
