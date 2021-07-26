def MulAdd(a,b):
	m=a*b
	s=a+b
	return m,s

x=int(input('Enter first number'))
y=int(input('Enter second number'))

res1,res2 = MulAdd(x,y)
print("Multiplication and Sum of"+str(x)+" and "+str(y)+"are: ",end='')
print(res1,res2)