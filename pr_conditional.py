import math as m
x=int(input("Enter a number"))
y=input("Input a string of one char")[0]

if len(y)!=1:
    print("this block will never be executed as length of y will always be 1")
elif x%2==0:
    print("The number you entered is an even number")
    if m.sqrt(x)==x:
        print("the number is either 0 or 1")
    else:
        print("the number you entered is either less than 0 or grater than 1")
else:
    print("you entered an odd number")

