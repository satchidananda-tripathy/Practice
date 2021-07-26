#matrix operations can not be done by array so we need to conver array into a matrix first
from numpy import *
arr=array([[1,2,3,4,5,6],[4,5,6,7,8,9]])

m=matrix(arr)
print(m)

#you can separate numbers by space while declaring a matrix

m1=matrix('1 2 3;3 4 5;6 7 8')
print(m1)

print(m1.diagonal())
print(m1.max())

#matrix multiplication also can be done easily by a function
#enter two matrix and multiply without using predefined function.



