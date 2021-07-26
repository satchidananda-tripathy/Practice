#delete recurring characters from a string and print the new string

str=input("Enter a word")

lst=list(str)
s=[]

for i in range(len(lst)):
    srch=lst[i]
    cnt=0
    for j in range(i,len(lst)):
        if lst[j]==srch:
            cnt=cnt+1
    if cnt>1:
        lst.remove(srch)

print(lst)