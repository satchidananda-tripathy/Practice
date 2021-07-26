#Number of word in a sentence

str="Hello how are you"

cnt=0
for i in range(len(str)):
    if str[i]==' ':
        cnt=cnt+1
print("No of words in the sentence",cnt+1)