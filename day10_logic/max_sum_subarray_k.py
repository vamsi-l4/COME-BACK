nums=list(map(int,input("ENTER THE NUMS: ").split()))
k=int(input("Enter k: "))
windowsum=0
for i in range(k):
    windowsum+=nums[i]
max_sum=windowsum
for i in range(k,len(nums)):
    windowsum=windowsum-nums[i-k]+nums[i] #NEW SUM = OLD SUM - leaving + entering
    if windowsum>max_sum:
        max_sum=windowsum
print("Maximum sum:", max_sum)