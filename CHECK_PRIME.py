import math
global n
def find_prime(num):
    prime=True
    sq=math.sqrt(num)
    if sq.is_integer():
        prime=False
    else:
        divisors=[2,3,5,7]
        if not num in divisors:
          for i in divisors:
            if num%i == 0:
              prime=False
              break
        if num>10 and prime:
             for i in range(2,(n/2+1)):
                 if n%i==0:
                        return False
    if prime:
        return True
    else:
        return False

n=int(input('Enter a number'))
p=find_prime(n)
if p :
      print (n,'is prime')
else:
      print (n,'is not prime')