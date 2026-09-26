arr1 = list(map(int, input("Enter arr1: ").split()))
arr2 = list(map(int, input("Enter arr2: ").split()))
freq={}
for num in arr1:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
result=[]
for num in arr2:
    if num in freq:
        count=freq[num]
        for i in range(count):
            result.append(num)
        del freq[num]
remaining=list(freq.keys())
remaining.sort()
for num in remaining:
    count=freq[num]
    for i in range(count):
        result.append(num)
print("relative array:",result)                   