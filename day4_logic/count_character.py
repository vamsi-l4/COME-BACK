text=input("enter the text: ")
character=input("enter a character: ")
count=0
for ch in text:
    if ch==character:
        count+=1
print(count)    