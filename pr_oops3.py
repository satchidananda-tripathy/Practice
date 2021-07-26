class abc:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a+self.b
    def minus(self):
        return self.a-self.b

obj1 = abc(5,6)
obj2 = abc(20,11)

print(obj1.add())
print(obj2.minus())

