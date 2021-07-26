a=20
def test():
    add=id(a)
    print("Inside Test",a,add)

add=id(a)
print("Outside Test",a,add)
test()