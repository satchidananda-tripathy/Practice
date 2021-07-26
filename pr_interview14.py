#Connect two strings
str1=input("Enter first string")
str2=input("Enter second string")
str=[]
for i in range(len(str1)):
    str.append(str1[i])

for j in range(len(str2)):
    str.append(str2[j])

print("first string ",str1)
print("first string ",str2)

for k in range(len(str)):
    print((str[k]),end='')