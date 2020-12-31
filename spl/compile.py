import os

l = os.listdir(os.getcwd() + '/spl_progs')
for i in l:
    if '.spl' in i:
        print('./spl '+ os.getcwd() +'/spl_progs/'+ i)
        os.system('./spl '+ os.getcwd() +'/spl_progs/'+ i)

print("finish")