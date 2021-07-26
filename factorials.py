def factor(num):
    f=1
    for i in range(1,num+1):
        f = f*i
    return f
x=int(input('Enter a number?'))
print('factorial of ',x,'is  : ',factor(x))
