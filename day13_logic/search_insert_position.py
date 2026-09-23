numbers = list(map(int, input("Enter numbers: ").split()))
target=int(input("Enter the target: "))
left = 0
right = len(numbers) - 1
while left<=right:
    middle=left+right//2
    if numbers[middle]==target:
        print("found",middle)
        break
    elif target<numbers[middle]:
        right=middle-1
    else:
        left=middle+1
else:
    print("position",left)
numbers.insert(left,target)
print("new array",numbers)