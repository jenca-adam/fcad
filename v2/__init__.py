import keys
import encrypt
import decrypt
import cmd
def iencrypt(filename,key):
    with open(filename,'rb')as f:
        g=f.read()
    e=encrypt.encrypt(g)
    with open(filename,'wb')as f:
        f.write(e)
def idecrypt(filename,key):
    with open(filename,'rb')as f:
        e=f.read()
    d=decrypt.decrypt(e)
    with open(filename,'wb')as f:
        f.write(d)
def irandom_key():
    print(keys.new())

