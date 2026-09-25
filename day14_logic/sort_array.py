nums=list(map(int,input("enter the nums: ").split()))
for i in range(len(nums)):
    for j in range(len(nums)-1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
print("sorted array:",nums)