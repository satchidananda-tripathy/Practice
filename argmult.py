def sum_val(a,*b):
    sum=a
    for i in b:
        sum=sum+i
    return sum


#sum of values 1,2,3,4
print("The sum of 1,2,3,4 is ",sum_val(1,2,3,4))
#sum of values 10,20
print("The sum of 10,20 is ",sum_val(10,20 ))
#sum of values 10,18,20,11,13,24
print("The sum of 10,18,20,11,13,24 is ",sum_val(10,18,20,11,13,24))
