numbers = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))
found=False
for i in range(len(numbers)):
    total=0
    for j in range(i,len(numbers)):
        total+=numbers[j]
        if total==target:
            print("subarray found:")
            for k in range(i,j+1):
                print(numbers[k] , end=" ")
            found=True
            break
    if found:
        break
if not found:
    print('no subarray found')