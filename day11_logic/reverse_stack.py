text=input("enter the text: ")
stack=[]
for ch in text:
    stack.append(ch)
result=""
while stack:
    char=stack.pop()
    result+=char
print(result)    