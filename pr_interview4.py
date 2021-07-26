#Sort elements in a list in descending order (Use Bubble Sort)
# Explanation with example is at the last line

lst=[2,1,4,6,3]

print("The list before sorting",lst)

for i in range(len(lst)-1):
    for j in range(len(lst)-1-i):
        if lst[j]<lst[j+1]:
            tmp=lst[j]
            lst[j]=lst[j+1]
            lst[j+1]=tmp

print(lst)
