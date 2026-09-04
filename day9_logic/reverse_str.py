text=list(input("enter the text: "))
left=0
right=len(text)-1
while left<right:
    temp=text[left]
    text[left]=text[right]
    text[right]=temp
    left+=1
    right-=1
print("reverse string:" , "".join(text))    
