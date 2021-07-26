class abc:
    def __init__(self,a):
         self.a=a
    def config(self):
        print("Hello ",self.a)

a = abc('Ram')
b=abc('Shyam')
a.config()
b.config()