text=input("enter the sentences: ")
word=text.split()
result=" "
for i in range(len(word)-1,-1,-1):
    result+=word[i]+' '
print(result)    
