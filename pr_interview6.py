##FIBONACII Series

i,j=1,1


num=int(input("How many numbers you want to print"))
print('0',' ','1',end='')
for l in range(2,num):
    next = i + j
    print(next,' ',end='')
    i=j
    j=next