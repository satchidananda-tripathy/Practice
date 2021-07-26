#print all the numbers which are divisible by 2 from the list. If none of them are divisible by 2 print 'No such numbers'

num=int(input("How many numbers you want to enter into the list, max 7 numbers you can enter "))
lst=[0,0,0,0,0,0,0]
if num>7:
    print("You can not enter more than 7 numbers")
    exit()
for i in range(0,num,1):
    lst[i]=int(input("Enter a number"))

for x in lst:
    if x%2==0:
        print(x)
        break
else:
    print("No such number")


