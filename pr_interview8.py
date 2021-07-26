#check if a list is palindrome or not

lst=[1,2,3,2,1]
lst1=[]

for i in range(len(lst)-1,-1,-1):
    lst1.append(lst[i])

print(lst)
print(lst1)

if lst==lst1:
    print("Palindrome")
else:
    print("Not a palindrome")