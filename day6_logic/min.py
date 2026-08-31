num=list(map(int,input("enter the num: ").split()))
smallest=num[0]
for nums in num:
    if nums<smallest:
        smallest=nums
print(smallest)        