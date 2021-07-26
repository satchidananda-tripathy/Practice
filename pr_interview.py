#Sort elements in a list in descending order (Use Selection Sort)
# Explanation with example is at the last line

a = [64,25,12,22,5,11,89,11]

for i in range(len(a)-1):
    pos = i
    for j in range(i,len(a)):
        if a[j]<a[pos]:
            pos=j


    temp=a[j]
    a[j]=a[pos]
    a[pos]=temp

print(a)



'''
arr[] = 64 25 12 22 11

// Find the minimum element in arr[0...4]
// and place it at beginning
11 25 12 22 64

// Find the minimum element in arr[1...4]
// and place it at beginning of arr[1...4]
11 12 25 22 64

// Find the minimum element in arr[2...4]
// and place it at beginning of arr[2...4]
11 12 22 25 64

// Find the minimum element in arr[3...4]
// and place it at beginning of arr[3...4]
11 12 22 25 64 
'''