#!/usr/bin/env python
from v2 import *
import cmd,v2.keys
class CmdLine(cmd.Cmd):
    def do_encrypt(self,line):
        file,keyfile=tuple(line.split(' '))
        iencrypt(file,v2.keys.analyze(open(keyfile,'rb')))
    def do_decrypt(self,line):
        file,keyfile=tuple(line.split(' '))

        idecrypt(file,v2.keys.analyze(open(keyfile,'rb')))
    def do_new_key(self,keyfile):
        with open(keyfile,'wb')as f:
            f.write(v2.keys.dump(v2.keys.new(),255))
    def do_EOF(self,FOO):
        print('')
        exit()
if __name__=='__main__':
    
    CmdLine().cmdloop()
