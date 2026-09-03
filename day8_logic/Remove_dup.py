n=list(map(int,input("enter the nums: ").split()))
seen=set()
for nums in n:
    if nums in seen:
        continue
    seen.add(nums)
print(seen)