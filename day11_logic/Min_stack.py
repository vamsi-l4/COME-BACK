stack=[]
min_stack=[]
n=int(input("how many nums: "))
for i in range(n):
    num=int(input("enter the nums: "))
    stack.append(num)
    if len(min_stack)==0:
        min_stack.append(num)
    elif num <= min_stack[-1]:
        min_stack.append(num)
print("stack: ",stack)
if len(min_stack) >0:
    print("minimum: ",min_stack[-1])