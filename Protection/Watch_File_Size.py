import os, sys , time
from playsound import playsound
filee = input("Enter PATH file :")
filesize = os.path.getsize(filee)
print (filesize)
while filesize == 57 :
    print("[OK] : " + time.ctime())
    time.sleep(1)
    filesize = os.path.getsize(filee)
else:
    warning = '''\033[31m
    [=====================]
    [   WRONG O THERE     ]
    [        IS           ]
    [      HA CKERS       ]
    [=====================]
    '''
    print(warning)
    playsound('E:\\police.mp3')
