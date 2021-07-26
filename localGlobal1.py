a=20
def test():
    a=10
    add=id(a)
    add_g=globals()['a']
    print("Inside Test",a,"Address of local",add)
    print("Inside Test",a,"ADDRESS OF Globnal",id(add_g))

test()
