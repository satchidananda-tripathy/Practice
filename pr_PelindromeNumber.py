#Check if a word is pelindrome or not

num=int(input("Enter a Number"))
beforerev=num
##String is immutable so we need to convert it to a list to store it's reverse
rev=0
while num!=0:
    rev=10*rev+num%10
    num=num//10

print("Reverse of the number is ",rev)

if rev==beforerev:
    print("Palindrome")
else:
    print("Not a palindrome")