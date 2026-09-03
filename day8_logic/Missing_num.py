nums=list(map(int,input("enter the nums: ").split()))
n=len(nums)
exists=set(nums)

for num in range(n+1):
    if num not in exists:
        print("Missing number:",num)
        break
result=[]
for num in range(n+1):    
    result.append(num)
print(result)   

