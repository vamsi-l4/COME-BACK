text=input("enter brackets: ")
stack=[]
pairs={")":"(",
       "]":"[",
       "}":"{"
       }
for char in text:
    if char in "([{":
        stack.append(char)
    else: 
        if not stack:
            print(False)
            break
        if stack[-1]!=pairs[char]:
            print(False)
            break
        stack.pop()
else:
    if not stack:
        print(True)
    else:
        print(False )                    