## An array is called as list in python it is mutable

lst=[1,2,'a',20]

print(lst)

print(len(lst))

lst[0]='x'

print(lst)

lst[0:2]=['x','y']

print(lst)

lst1=['Hi',"Hello",'Namaste']

print(lst+lst1)

lst2=[['a','b'],['1',2]]

print(lst2)

### Functions for List

print(lst.append('45'))
print("\n")
print(lst)

lst.remove(20)

print(lst)

lst.insert(2,22)

print(lst)

lst.pop()

print(lst)

lst.pop(1)
print(lst)

print("\n")
print(lst1)

del lst1[1:]
print(lst1)

lst1.extend(['a','b','c'])
print(lst1)

lst1.append(['a','v']) ## This will take the list as an element to be added in the list
print(lst1)

nums=[1,2,3,4,7,5]
print(min(nums))


print(max(nums))
print(sum(nums))

nums.sort()
print(nums)

## Multi dimensional

lst4=[['a','b'],['c','d']]
print(lst4)

print(lst4[1][0])

