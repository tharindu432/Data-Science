f=open("c://L2S2/funny.txt","w")
f.write("\ni lovr python")
f.close()


#exceptiom handling

x=input("enter number 1: ")
y=input("enter number 2: ")
try:
  z=int(x)/int(y)
  print(z)
except Exception as e:
  print("exception occured! :",e)


#exception handling in a function

a=input("enter number 1: ")
b=input("enter number 2: ")

def cal_div(x,y):

    try:
        return int(x)/int(y)
    except ZeroDivisionError as e:
        print("error occured!:", e)
        return None
    except TypeError as e:
        print("type error exception")
        return None

print(cal_div(a,b))















