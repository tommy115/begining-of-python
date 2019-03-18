from datetime import date
import sys

print("############### 10-1 ###############")
file_name = "today.txt"
with open(file_name,"wt") as fout:
    fout.write(date.today().isoformat())

print("############### 10-2 ###############")
with open(file_name,"rt") as fin:
    lines = fin.readlines()

if len(lines) == 1:
    today_string = lines[0]
else:
    print("this is error")
    sys.exit()

print("############### 10-3 ###############")
import re, time

#### pattern 1
today = date( int(re.split("-",today_string)[0]),
              int(re.split("-",today_string)[1]),
              int(re.split("-",today_string)[2]))
print(today)

#### pattern 2
fmt = "%Y-%m-%d"
#today = date.strptime(today_string,fmt)
mytoday = time.strptime(today_string,fmt)
today = date( mytoday.tm_year, mytoday.tm_mon, mytoday.tm_mday )
print(today)

print("############### 10-4 ###############")
import os

dirlist = os.listdir('.')
print(dirlist)

print("############### 10-5 ###############")
pdirlist = os.listdir('..')
print(pdirlist)

print("############### 10-6 ###############")
import multiprocessing as mp
import random
import time

def do_this(n):
    print("pid:{0} sleep {1}sec".format(os.getpid(),n))
    time.sleep(n)

for n in range(3):
    rand = random.randrange(5)
    process = mp.Process(target=do_this, args=(rand,))
    process.start()

print("############### 10-7,10-8 ###############")
bday = date(1974, 1, 15)
fmt = "%A"
print(bday.strftime(fmt))

print("############### 10-9 ###############")
from datetime import timedelta
delta = timedelta(days=10000)
afterdays = bday + delta
print(afterdays)
