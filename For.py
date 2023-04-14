exp = [2340,3400,5600,7666,4543,6767]
total=0
for item in exp:
    total=total+item
print(total)

#range function

for i in range(1,10):
    print(i)

#len function
for i in range(len(exp)):
    print("your total expence of ",(i+1),"month is",exp[i])
print("total expense is: ",total)

#example
key_location ='chair'
locations= ["garage","living room","chair","closet"]

for i in locations:
    if i==key_location:
        print("key location in: ",i)
        continue
    else:
        print("key is not found in",i)

#functions
tom_exp=[2100,6789,9000]
joe_exp=[5678,9321,5000]
total_exp=0
for item in tom_exp:
    total_exp=total_exp+item
print("total expenses of tom are:",total_exp)

