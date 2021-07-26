#enter a number from keyboard and print the position by binary search.
# To perform binary search , the array should be in sorted order.

lst=[99,1,2,3,4,5,6]
lst.sort()

print(lst)

k=int(input("Enter a number to search"))

startpos=0
lastpos=len(lst)

for i in range(len(lst)):
    pos = (startpos + lastpos) // 2
    if lst[pos]==k:
        print("Found at position",pos)
        break;
    elif lst[pos]<k:
         startpos=pos
    else:
        lastpos=pos
else:
    print("Not found")

print("End of the Program")


