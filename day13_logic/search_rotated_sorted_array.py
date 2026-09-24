numbers = list(map(int, input("Enter rotated sorted numbers: ").split()))
target = int(input("Enter target: "))
left = 0
right = len(numbers) - 1
while left <= right:
    middle = (left + right) // 2
    if numbers[middle]==target:
        print("found",middle)
        break
    if numbers[left]<=numbers[middle]:
        if numbers[left]<=target<numbers[middle]:
            right=middle-1
        else:
            left=middle+1
    else:
        if numbers[middle]<=target<numbers[right]:
            left=middle+1
        else:
            right=middle-1
else:
    print("not found")             