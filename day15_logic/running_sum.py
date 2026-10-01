nums=list(map(int,input("enter the nums:").split()))
prefix=[]
total=0
for num in nums:
    total+=num
    prefix.append(total)
print("prefix sum:",prefix)