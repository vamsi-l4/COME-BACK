nums=list(map(int,input("enter the nums:").split()))
prefix=[]
total=0
for num in nums:
    total+=num
    prefix.append(total)
left=int(input("enter left index: "))
right=int(input("enter right index: "))
if left==0:
    ans=prefix[right]
else:
    ans=prefix[right]-prefix[left-1]
print("Prefix sum:", prefix)
print("Range sum:", ans)