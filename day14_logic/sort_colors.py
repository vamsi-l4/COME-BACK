numbers = list(map(int, input("Enter colors: ").split()))
count0 = 0
count1 = 0
count2 = 0
for number in numbers:
    if number == 0:
        count0 += 1
    elif number == 1:
        count1 += 1
    elif number == 2:
        count2 += 1

result = []

for i in range(count0):
    result.append(0)
for i in range(count1):
    result.append(1)
for i in range(count2):
    result.append(2)
print("Sorted colors:", result)