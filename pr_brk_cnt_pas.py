#Enter a number and print all the even numbers from 1 to that number. Make sure to print untill 25.

n=int(input("Enter a number"))

for x in range(n):
    if x>=25:
        print ("Out of range")
        break
    if x%2!=0:
        continue
    print(x,' ',end='')

def futurefun():
    pass

futurefun()

print()
print("above function doesn't do anything just kept to implement in future")
print("Bye")