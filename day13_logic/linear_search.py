numbers = list(map(int, input("Enter numbers: ").split()))
target=int(input("Enter the target: "))
found=False
for i in range(len(numbers)):
    if numbers[i]==target:
        print("Founded:",i)
        found=True
        break
if found==False:
    print("not found")    