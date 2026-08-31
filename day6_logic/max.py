num=list(map(int, input("enter the nums: ").split()))
biggest=num[0]
for nums in num:
    if nums>biggest:
        biggest=nums
print(biggest)        
