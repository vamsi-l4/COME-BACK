num=list(map(int,input("enter the num: ").split()))
set=[]
for nums in num:
    if nums not in set:
        set.append(nums)
print(set)        