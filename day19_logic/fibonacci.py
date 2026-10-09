n=int(input("enter nums: "))
a=0
b=1
for i in range(n):
    print(a,end=' ')
    next_sum=a+b
    a=b
    b=next_sum