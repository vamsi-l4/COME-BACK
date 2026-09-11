text=input("enter the string: ")
seen=set()
left=0
max_len=0
for right in range(len(text)):
    char=text[right]
    while char in seen:
        seen.remove(text[left])
        left+=1
    seen.add(char)
    length=right-left+1
    if length>max_len:
        max_len=length   
print(max_len)