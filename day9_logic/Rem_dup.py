nums=list(map(int,input("enter the nums: ").split()))
k=1
for i in range(1,len(nums)):
    if (nums[i]!=nums[i-1]):
        nums[k]=nums[i]
        k+=1
print("unique values: ",nums[:k])    