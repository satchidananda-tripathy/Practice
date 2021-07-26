a,b=10,7
def lcl():

    a=5
    print("value of local variable",a)
    print("value of global variable a accessed within local", globals()['a'])
    print("value of global variable b accessed within local", globals()['b'])
lcl()
print("value of global variable",a)