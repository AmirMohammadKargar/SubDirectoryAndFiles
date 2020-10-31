from pathlib import Path
import os
from os import listdir
from os.path import isfile, join
print("Directory Path:", Path().absolute())  
def showDir(num ,dirs,des):
    if des !='.':
        print("|__"+des)
    try:
        onlyfiles = [f for f in listdir(dirs) if isfile(join(dirs, f))]
        for files in onlyfiles:
            for i in range(0,num):
                print('  ',end="")
            print("|__"+files[0:])
    except Exception as err:
        pass
    dis = []
    try:
        subdirs = os.listdir(dirs)
        for item in subdirs:
            if '.' not in item:
                dis.append(item)
        for dirse in dis:
            for i in range(0,num):
                print('  ',end="")
            n = num+1
            showDir(n,dirs+'/'+dirse,dirse)
    except Exception as err:
        pass
showDir(0,'.','.')
