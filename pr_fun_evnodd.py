#pass a list to a function and print the number of odd and evens in it

def prntenvod(lst):
    evn,od=0,0
    for itm in lst:
        if itm%2==0:
            evn+=1
        else:
            od+=1
    return evn,od

lst=[1,2,3,4,5,6,7,8,9]
x,y = prntenvod(lst)
print("No of even {} and No of odd {}".format(x,y))