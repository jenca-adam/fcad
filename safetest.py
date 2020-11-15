#!/usr/bin/env python
import os 
os.chdir('..')
import fcad
sh=fcad.SafeHasher('cina.fcadk')
sh.decodekeyfile()
sh.codefile('cina.png')
d=fcad.Decoder('cina.fcadk')
d.decodekeyfile()
d.decodefileby()
