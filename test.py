from numpy import *
def abc(val,y=[]):
    y.append(val)
    return y
print(abc(3))
print(abc(4,[1,2]))
print(abc(10))