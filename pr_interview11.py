#Print repeated characters in a word, also pring how many times it got repeated

#Print the duplicate numbers from a list
str=input("Enter a word")

lst=list(str)
s=[]
t=()

for i in range(len(lst)):
    srch=lst[i]
    cnt=0
    for j in range(i,len(lst)):
        if lst[j]==srch:
            cnt=cnt+1
    if cnt>1:
        s.append(srch)

print(set(s))