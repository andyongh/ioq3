import random

global keygen, intmap
keygen = ""
intmap = [
    "2",
    "3",
    "7",
    "a",
    "b",
    "c",
    "d",
    "g",
    "h",
    "j",
    "l",
    "p",
    "r",
    "s",
    "t",
    "w",
]


def percRandom():
    return random.randint(0, 16)


def gen():
    global keygen, keycount, intmap
    nbr = percRandom()
    if nbr < len(intmap):
        if len(keygen) == 16:
            done()
        keygen += str(intmap[nbr])
    gen()


def done():
    print("Key: " + keygen)
    exit()


gen()
