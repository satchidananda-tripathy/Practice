# Split a string based on delimiter

str=input("Enter a string , keep some delimiter in between")
dl=input("Which delimiter you passed")
pos=0
delimpos=[]
for i in range(len(str)):
    if str[i]==dl:
        delimpos.append(i)
print("No of delimiter",len(delimpos))

strtpos=0
for endpos in delimpos:
    print(str[strtpos:endpos],' ')
    strtpos=endpos+1

print(str[endpos+1:len(str)])

