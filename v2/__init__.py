from . import keys
from . import encrypt
from . import decrypt
def iencrypt(filename,key):
    with open(filename,'rb')as f:
        g=f.read()
    e=encrypt.encrypt(g,key)
    with open(filename,'wb')as f:
        f.write(bytes(e))
def idecrypt(filename,key):
    with open(filename,'rb')as f:
        e=f.read()
    d=decrypt.decrypt(e,key)
    with open(filename,'wb')as f:
        f.write(bytes(d))
def irandom_key():
    return keys.new()

