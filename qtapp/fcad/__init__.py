from . import keys
from . import encrypt
from . import decrypt
def iencrypt(filename,keyfile):
    try:
        with open(filename,'rb')as f:
            g=f.read()
    except FileNotFoundError:
        return 'EEFNF'

    try:
        key=keys.analyze(open(keyfile,'rb'))
    except FileNotFoundError:
        return 'EKFNF'

    e=encrypt.encrypt(g,key)
    
    

    with open(filename,'wb')as f:
        f.write(bytes(e))
def idecrypt(filename,key):
    try:
        with open(filename,'rb')as f:
            e=f.read()
    except FileNotFoundError:
        return 'DDFNF'
    try:
        key=keys.analyze(open(keyfile,'rb'))
    except FileNotFoundError:
        return 'DKFNF'

    d=decrypt.decrypt(e,key)
    with open(filename,'wb')as f:
        f.write(bytes(d))
def irandom_key(name):
    with open(name,'wb')as f:
            f.write(keys.dump(keys.new(),255))

