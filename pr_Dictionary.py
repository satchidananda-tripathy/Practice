# Dictionary is for key value pair.
#In a dictionary allthe keys must be unique. A key can not point to two separate value.

data={1:'Sachin',2:'Sourav',3:'Dravid',4:'Yuvraj'}

print(data)
print("\n")
print("The player with batting order 3  is : ",data[3])
print("The player with batting order 2 is : ",data.get(2))

#In python None meand null or nothing

print(data.keys())

print(data.values())

print(data.get(10))

#if not found we can pring a null value

print(data.get(2,"Not found "))

print(data.get(10,"Not found "))

## can we create a dictionary out of list ?

lst1=[1,2,3,4,5,6]
lst2=['a','b','c','d','e','f']
data=dict(zip(lst1,lst2))

print(data)

print(data[1])

# dictionary is mutable
data[5]='x'
print(data)
## delete data from dictionary
del data[1]
print(data)


##Mixed Dictionary

data2={1:['a','b'],3:{'x','y'},4:'99'}

print(data2)

#print(data2[2][2])
