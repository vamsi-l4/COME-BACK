num=list(map(int,input("enter the nums: ").split()))
reverse=[]
for nums in range(len(num)-1,-1,-1):
    reverse.append(num[nums])
print(reverse)    
# another approach 
num=list(map(int,input("enter the nums: ").split()))
reverse=[]
for nums in num[::-1]:
    reverse.append(nums)
print(reverse)