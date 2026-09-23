n = list(map(int, input("Enter numbers: ").split()))
firstbad=int(input("Enter first bad: "))
left = 1
right = len(n)
while left<=right:
    middle=(right+left)//2
    if middle>=firstbad:
        right=middle-1
    else:
        left=middle+1
print("firstbad:",left)