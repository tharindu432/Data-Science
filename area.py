
height= 6
base=8
area=1/2*base*height
print("area of our triangle is:",area)

#if statement

number1=input("enter the first number: ");
number2=input("enter the second number: ")

sum =int(number2)+int(number1)
#avg= (number2+number1)
avg = (int(number2)+int(number1))/2

if(sum%2==0) :
    print("sum is even")
else:
    print("sum is odd");
#print(avg)

indian=['samosa','daal','naaan'];
chineese=['egg role','pot sticker','fried rice']
italian=['pizza','pasta','risotto']

dish=input("enter the dish name:");

if dish in indian:
    print('your choice is inian food!')
elif dish in chineese:
    print("your choice is chinese food! ")
elif dish in italian:
    print("your choice is italian food!")
else:
    print("please enter correct dish!")
