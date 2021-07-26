def fibo(num):
    a,b=0,1
    print(a,b,end=" ")
    cnt=3
    while(cnt<=num):
        c=b+a
        print(c,end=" ")
        a=b
        b=c
        cnt=cnt+1

x=int(input('How many number from fibonacii series you need?'))
print('=============')
fibo(x)