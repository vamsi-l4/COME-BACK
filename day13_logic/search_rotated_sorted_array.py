numbers = list(map(int, input("Enter rotated sorted numbers: ").split()))

target = int(input("Enter target: "))

left = 0
right = len(numbers) - 1

while left <= right:

    middle = (left + right) // 2