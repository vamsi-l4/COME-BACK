text=input("enter the text: ")
count={}
for char in text:
    if char in count:
        count[char]+=1
    else:
        count[char]=1
for char in count:
    print(char,":",count[char])         