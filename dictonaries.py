
d={"tom":778071691,"tharindu":764492334,"chathuwa":771253346}

print(d)

print(d["tom"])
#insert

d["sam"]=760515861

print(d)

#delete
del d["tom"]

print(d)

for key in d:
    print("key: ",key,"value: ",d[key])

if("tharindu" in d):
    print("yes")
else:
    print("no")

#tuples
x=(10,8)


import math
math.sqrt(16)
print(math.sqrt(16))
print(math.pow(3,5))

print(dir(math))

c=7.3
d=math.floor(c)
e=math.ceil(c)
print(d)
print(e)
import calendar

cal= calendar.month(2021,1)
print(cal)

