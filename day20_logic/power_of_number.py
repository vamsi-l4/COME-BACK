def power(base,exponent):
    if exponent==0:
        return 1
    return base*power(base,exponent-1)
base=int(input("enter base: "))
exponent=int(input("enter exponent: "))

print(power(base,exponent))