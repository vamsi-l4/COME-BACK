num=list(map(int,input("enter the nums: ").split()))
target=int(input("enter the target: "))
left=0
right=len(num)-1
while left<right:
    total=num[left]+num[right]
    if total==target:
        print("The pair numbers:",num[left],num[right])
        break
    elif total<target:
        left+=1
    else:
        right-=1