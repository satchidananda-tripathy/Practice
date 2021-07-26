#Check if a word is pelindrome or not

str=input("Enter a word")

##String is immutable so we need to convert it to a list to store it's reverse
lst=list(str)

lst1=[]

for i in range(len(lst)-1,-1,-1):
    lst1.append(lst[i])

print(lst)
print(lst1)

if lst==lst1:
    print("Palindrome")
else:
    print("Not a palindrome")