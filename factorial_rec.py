def factor(num):
    if num==0:
        return 1
    else:
        return num*factor(num-1)

x=int(input('Enter a number?'))
print('factorial of ',x,'is  : ',factor(x))
