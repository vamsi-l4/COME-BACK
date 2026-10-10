# num=int(input("enter nums: "))
# total=0
# while num>0:
#     digit=num%10
#     total+=digit
#     num=num//10
# print(total)
def sum_digits(n):
    if n==0:
        return 0
    digit=n%10
    remaining=n//10
    return digit+sum_digits(remaining)
n=int(input("enter nums: "))
print(sum_digits(n))
