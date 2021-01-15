

import random
from .perms import cyclic
def new():
    shuffle=list(range(255))
    random.shuffle(shuffle)
    lines=cyclic(shuffle)
    random.shuffle(lines)
    return lines

