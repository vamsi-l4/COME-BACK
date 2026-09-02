num=list(map(int,input("enter the num: ").split()))
target=int(input("enter the target: "))
seen={}
for i in range(len(num)):
    current=num[i]
    needed=target-current
    if needed in seen:
        print(seen[needed],i)
        break
    else:
        seen[current]=i