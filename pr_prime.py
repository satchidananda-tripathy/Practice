import math as m
#enter and number and check if it is prime or not

num=int(input("Enter a number"))
for i in range(2,num,1):
    if num%i==0:
        print("Composite")
        break
else:
    print("Prime")

#Below is efficient logic
#Find out square root on num. Traverse all odd numbers up to the sqrt(N)
#and try to devide the num with current odd number. If remainder is 0 for any odd number then number is NOT PRIME. Else – number is PRIME.

print("Below output is with logic 2")
sq=int(m.sqrt(num))


for i in range(1,sq,2):
    if (sq%i==0):
            print("composite")
            break
else:
    print("Prime")
