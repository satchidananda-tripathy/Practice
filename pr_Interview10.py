#Print the duplicate numbers from a list

lst=[1,2,3,4,2,3,2,1]
s=[]

for i in range(len(lst)):
    srch=lst[i]
    cnt=0
    for j in range(i,len(lst)):
        if lst[j]==srch:
            cnt=cnt+1
    if cnt>1:
        s.append(srch)

print(set(s))