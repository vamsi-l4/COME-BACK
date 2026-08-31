num=list(map(int,input("enter the nums: ").split()))
count=0
target=int(input("enter the target: "))
for nums in num:
    if nums==target:
        count+=1
print(count)