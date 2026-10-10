def count_digits(n):
    if n<10:
        return 1
    return 1+count_digits(n//10)
n=int(input("enter nums: "))
print(count_digits(n))