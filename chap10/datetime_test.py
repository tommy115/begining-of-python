from datetime import date

hello = date(2014, 10, 31)
print(dir(hello))
print(hello)
print(hello.day)
print(hello.month)
print(hello.year)
print(hello.isoformat())

print("###################")
now = date.today()
print(now)

print("###################")
from datetime import timedelta
one_day = timedelta(days=1)
print(dir(one_day))
tomorrow = now + one_day
print(tomorrow)
print(now + 17 * one_day)
yesterday = now - one_day
print(yesterday)

print("###################")
from datetime import time
noon = time(12, 0, 0)
print(dir(noon))
print(noon)
print(noon.isoformat())
print(noon.hour)
print(noon.minute)
print(noon.second)
print(noon.microsecond)

print("###################")
from datetime import datetime
some_day = datetime(2014, 1, 2, 3, 4, 5, 6)
print(some_day)
print(some_day.isoformat())
import re
print(re.split("[-T]",some_day.isoformat()))

now = datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)



