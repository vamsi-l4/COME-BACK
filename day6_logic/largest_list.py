num=list(map(int,input("enter the num: ").split()))

largest=None
second_largest=None
for nums in num:
    if largest is None or nums>largest:
        second_largest=largest
        largest=nums
    elif nums!=largest and (second_largest is None or nums>second_largest):
        second_largest=nums
print(second_largest)            
