## Tuples are immutable within round bracket

## we can create project static variables with in tuples
## as it is immutable the iteration in tuple is faster than list

tup=(1,2,3,4,5)

print(len(tup))

print(tup[1:])

#tup[1]=5 it will not work as it is immutable



#Strings are immutable

str="Hello"
print (str[0])

#str[0]='F'
##Above statemnt will throw error as str is immutable

#Underscore means output of the previous operation
x,y=5,6
x=x+5

print(x,y)

print ("Length of string is ",len(str))

####

## Set are collection of Unique elements

S={1,2,3,4,3,2,56,23}

print(S)

## set don't store values with sequence so we can not fetch data from sets by position or index

##we can pop, remove add data in set

S.add('a')
print(S)

