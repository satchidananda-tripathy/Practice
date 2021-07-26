class people:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def compare(self,othobj):
        if othobj.age==self.age:
            return True
        else:
            return False

p1 = people("Sachin",39)
p2 = people("Suresh",40)

if(p1.compare(p2)):
    print("Their age is same")
else:
    print("Their age is different")

