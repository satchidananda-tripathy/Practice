#
##
###
####
#####

print("-------Using For loop-----")
## Using For loop
for r in range(1,5,):
    for c in  range(r):
        print("*",end='')
    print()

print("-------Using while loop-----")
## Using while loop
r=1
while(r<5):
    c=1
    while(c<=r):
        print ('*',end='')
        c=c+1
    r=r+1
    print()

print("end of program")