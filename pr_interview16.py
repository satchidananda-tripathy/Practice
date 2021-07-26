#print number of alphabet and number of numerics and number of symbol in a string.
str="Hell*&012abc"
ch,num,sym=0,0,0
for c in str:
    if c.isalpha():
        print("alphabet",c)
        ch=ch+1
    elif c.isnumeric():
        print("Numeric",c)
        num=num+1
    else:
        print("symbol",c)
        sym=sym+1

print("Total number of symbol ",sym ," alphabet",ch,"numeric ",num)
