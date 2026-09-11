nums=list(map(int,input("Enter the nums: ").split()))
k=4
Windowsum=0
for i in range(k):
    Windowsum+=nums[i]
max_sum=Windowsum
for i in range(k,len(nums)):
    Windowsum=Windowsum-nums[i-k]+nums[i]
    if Windowsum>max_sum:
        max_sum=Windowsum
print("Maximum average:", max_sum/k)