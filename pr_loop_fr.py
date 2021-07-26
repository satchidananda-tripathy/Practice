x=range(10)
lst=list(x)
for i in lst:
    print(i,' ',end='')
    j=5
    while(j>=i):
        print(j,end='')
        j-=1
    print()