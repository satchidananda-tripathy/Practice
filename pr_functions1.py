def add(x,y):
    return x+y

a,b=5,6
print(add(a,b))

### Default argumenet
def sumation(a,b,c=0):
    return a+b+c

print(sumation(2,3))
print(sumation(2,3,4))

##variable length argument
print("if you pass multiple arguments and you don't know how many ")

def add(*arg):
    result=0
    for k in arg:
        result=result+k
    return result

print(add(1,2,3,4,5))

print("Pass argument name i.e. key as well as value into function and print both key and value")
def prt(**kw):
    for i,j in kw.items():
        print(i,j)

prt(name='sachin',age=5,address="bbsr")

