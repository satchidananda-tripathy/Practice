#this will not work
def factorials(N):
    res=1
    for i in range(1,N+1):
        res*=i
    return res

n=int(input('enter a no'))
x=factorials(n)
print(x)