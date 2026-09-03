n=list(map(int,input("enter the nums: ").split()))
seen=set()
duplicate=False
for nums in n:
    if nums in seen:
        duplicate=True
        break
    seen.add(nums)
print(duplicate)    