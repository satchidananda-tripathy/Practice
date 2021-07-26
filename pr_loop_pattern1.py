#####
####
###
##
#

#Using For Loop

for r in range(1,5,1):
    for c in range(0,5-r,1):
        print('*',end='')
    print()

#Using while loop
r=1
while r<=5:
    c=0
    while(c<=5-r):
        print('*',end='')
        c=c+1
    r=r+1
    print()