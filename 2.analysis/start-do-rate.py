
#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from multiprocessing import Process
import os
import time
import sys
s=int(sys.argv[1])
sd=int (sys.argv[2])
def StartSh(path):
    os.system(path)

if __name__ == '__main__':
        cd=1
        sh1 = "pkill -9 -f python"

        sh2='/home/wonderful/.virtualenvs/mario_venv/bin/python -u /home/wonderful/workspace/wonderful/kensontest2/loltwgg/appkenson/f4/do-rate.py '
        li = [sh2,sh1]
        a=['8.11','8.10','8.12','8.9']
        for i in range(1,15):
            start1=str(i*10-s)
            end1=str(i*10-sd+1)
            p = Process(target=StartSh, args=(sh2+a[2]+' '+start1+' '+end1,))
            p.start()


