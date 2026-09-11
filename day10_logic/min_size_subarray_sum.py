nums=list(map(int,input("Enter the nums: ").split()))
target=int(input("Enter target: "))
left=0
current_sum=0
min_len=len(nums)+1
for right in range(len(nums)):
    current_sum+=nums[right]
    while current_sum >= target:
        length=right-left+1
        if length<min_len:
            min_len=length
        current_sum-=nums[left]
        left+=1
if min_len==len(nums)+1:
    print(0)
else:
    print(min_len)