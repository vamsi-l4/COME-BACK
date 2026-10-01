nums=list(map(int,input("enter the nums:").split()))
total=0
for num in nums:
    total+=num
left=0
for i in range(len(nums)):
    current=nums[i]
    right=total-left-current
    if left==right:
        print("pivot index:",i)
        break
    left+=current
else:
    print("no pivot index")
