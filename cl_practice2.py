class person:
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight

    def printdetails(self):
        print(self.name+"'s  height is "+str(self.height))
        print(self.name+"'s  weight is "+str(self.weight))

ram = person('ram',6,61)
ram.printdetails()

shyam = person('shyam',6.5,71)
shyam.printdetails()