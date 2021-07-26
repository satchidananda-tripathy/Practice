# Enter a word e.g. Apple and print as follows
#A
#Ap
#App
#Appl
#Apple

str=input("Enter a word")
for i in range(0,len(str),1):
    for j in range(i+1):
        print(str[j],end='')
    print()
#A
#pp
#ppp
#llll
#eeee
for i in range(0,len(str),1):
    for j in range(i+1):
        print(str[i],end='')
    print()