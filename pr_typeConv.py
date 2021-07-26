x=5.2
print(x)

y=int(x)
print(y)

ls=[1,2,3]
print(ls)

tp=tuple(ls)
print(tp)

c=complex(x,y)
print(c)

ls1=list(tp)
print(ls1)

ls2=['a','b','c']

data1=dict(zip(ls,ls2))
print(data1)

data2=dict(zip(tp,ls2))
print(data2)

tpl=tuple(range(10))
print(tpl)

lst11=list(tpl)
print(lst11)