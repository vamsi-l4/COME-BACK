nums1=list(map(int,input("enter 1st nums: ").split()))
nums2=list(map(int,input("enter 1st nums: ").split()))
seen=set(nums1)
result=[]
for nums in nums2:
    if nums in seen:
        if nums not in result:
            result.append(nums)
print(result)        