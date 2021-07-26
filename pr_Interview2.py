#prime numbers between 100 and 200
#Logic : Pick a number and keep multiplying from 2 to that number-1 and if any number divisible it is composite so break

for num in range(100,200,1):
    for i in range(2,num):
        if num%i == 0:
            break
    else:
        print(num)

