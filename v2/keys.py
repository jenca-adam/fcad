

import random
from .perms import cyclic
def new():
    shuffle=list(range(256))
    random.shuffle(shuffle)
    lines=cyclic(shuffle)
    random.shuffle(lines)
    return lines
def dump(key,s):
    b=[s]
    for sub in key:
        for subsub in sub:
            b.append(subsub)
    return bytes(b)

def analyze(file):
    s=256
    file.seek(1)
    k=[]
    while len(k)<256:
        k.append(list(file.read(s)))
    return k
