import os

l = os.listdir(os.getcwd() + '/spl_progs')
for i in l:
    if '.spl' in i:
        print('./spl '+ os.getcwd() +'/spl_progs/'+ i)
        os.system('./spl '+ os.getcwd() +'/spl_progs/'+ i)


l = os.listdir(os.getcwd() + '/spl_progs/s15')
for i in l:
    if '.spl' in i:
        print('./spl '+ os.getcwd() +'/spl_progs/s15/'+ i)
        os.system('./spl '+ os.getcwd() +'/spl_progs/s15/'+ i)

print("finish")