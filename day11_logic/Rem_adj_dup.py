text=input("enter the text: ")
stack=[]
for ch in text:
    if len(stack)==0:
        stack.append(ch)
    elif stack[-1]==ch:
        stack.pop()
    else:
        stack.append(ch)
print("".join(stack))        