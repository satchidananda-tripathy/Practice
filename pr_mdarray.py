from numpy import *
arr=array([[1,2,3,4,5,6],[4,5,6,7,8,9]])

print(arr)
print(arr.dtype)

print(arr.ndim)
print(arr.shape)

arr1=arr.flatten()
print(arr1)

arr2=arr.reshape(2,3,2)
print(arr2)

arr4=array([[1,2,3,4,5,6],[4,5,6,7,8,9]])

arr5=arr1+arr4
print(arr5)

