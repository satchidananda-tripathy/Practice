#Variables in Python
#We don't have to specify the type in python

a=5
print(a)

## print address of variable -- Remember that Value has an address. variable just point to it.

print("address of 5 is ", id(a))

b=5
print("address of 5 is ",id(b))

print("\n---------------")
a="Hello"

print("address of Hello is ",id(a))

x=a

print("address of Hello is ",id(x))

print("Data type of the variable X is ",type(x))
## if a value is assigned to a variable but later the value got changed then the unused memory from first value moved to garbage colleciton.


#In python we can not create static variable but we can show intention by capitalizing it's name

PI=3.14
print(PI)
