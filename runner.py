#!/usr/bin/env python
from v2 import *
class CmdLine(cmd.Cmd):
    def do_encrypt(self,file,key):
        iencrypt(file,key)
    def do_decrypt(self,file,key):
        idecrypt(file,key)
    def do_new_key(self):
        print(irandom_key)
    def do_EOF(self):
        print('')
        exit()
if __name__=='__main__':
    CmdLine.cmdloop()
