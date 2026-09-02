text=input("enter the text: ")
unique={}
for char in text:
    if char in unique:
        unique[char]+=1
    else:
        unique[char]=1
for char in unique:
    if unique[char]==1:
        print(char)            
        break