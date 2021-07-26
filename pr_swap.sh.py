x,y=10,20
print("before swap",x,y)
x=x+y
y=x-y
x=x-y

print("after swap",x,y)

a,b=2,3
print("before swap",a,b)
temp=a
a=b
b=temp

print("after swap",a,b)

##Using xor
x,y=11,23
print("before swap",x,y)
x=x^y
y=x^y
x=x^y

print("after swap",x,y)

## Special in Python

x,y=31,71
print("before swap",x,y)
x,y=y,x

#EXPLANATION : IN THE STACK IT WILL WORK FROM RIGHT TO LEFT. It works with the concept of Rot2 in python
print("after swap",x,y)