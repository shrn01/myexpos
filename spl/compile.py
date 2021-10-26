#!/usr/bin/env python3

import os

# get all immediate subdirectories of /sql_progs directory
dir = [ '/' + x for x in next(os.walk(os.getcwd() + '/spl_progs'))[1]]  

# add /sql_progs directory
dir.append('')

for i in dir:
    print('\nin directory ' + os.getcwd() + '/spl_progs' + i)
    l = os.listdir(os.getcwd() + '/spl_progs' + i)
    for k in l:
        if '.spl' in k:
            print('\tcompiling '+ os.getcwd() + '/spl_progs'+ i + '/' + k)
            os.system('./spl '+ os.getcwd() + '/spl_progs'+ i + '/' + k)

print("finished compiling")