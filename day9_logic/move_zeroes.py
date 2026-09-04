nums=list(map(int,input("enter the nums: ").split()))
k=0
for i in range(1,len(nums)):
    if nums[i]!=0:
        nums[k]=nums[i]
        k+=1
for i in range(k,len(nums)):
    nums[i]=0
print(nums)