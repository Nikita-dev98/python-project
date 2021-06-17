#!bin/bash/python

from datetime import datetime

d1 = input("Enter a date (i.e. 2017,7,1)")
year,month,day = map(int,d1.split(','))
date_1 = datetime(year,month,day)

d2 = input("Enter 2nd date (i.e. 2017,7,1)")
y1,m1,d1 = map(int,d2.split(','))
date_2 = datetime(y1,m1,d1)

diff = date_2 - date_1

print("\ntime left:")
print(diff)
print(diff.days)