##enter few numbers into an array then search a particular number (entered) within the array.
# array module in python doesn't support multidimensional array

from array import *

ar=array('i',[]) #This is an integer array


cnt=int(input("how many number you want to enter into the array"))
for num in range(0,cnt,1):
    ar.append(int(input("Enter a number")))

for n in range(len(ar)):
    print(ar[n],' ',end='')

srch=int(input("Enter the number to search"))

for i in range(0,len(ar),1):
    if ar[i]==srch:
        print("Found at location ",i)
        break
else:
    print("Not found in the array")