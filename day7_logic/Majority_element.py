num=list(map(int,input("enter the nums: ").split()))
count={}
for nums in num:
    if nums in count:
        count[nums]+=1
    else:
        count[nums]=1
Majority=None
for nums in count:
    if count[nums]>len(num)/2:
        Majority=nums
        break            

if Majority is None:
    print("No Majority element")
else:
    print("Majority element:", Majority)    