#!/usr/bin/env python3
import os
try:
    with open('fcad.py')as fcad:
        os.chdir('/usr/bin')
        with open('fcad','w')as f:
            f.write(f.read())
except PermissionError:
    print('You must be a superuser to install FCaD')
        
