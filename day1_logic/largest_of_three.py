num1=int(input("enter the number:"))
num2=int(input("enter the 2nd number"))
num3=int(input("enter the 3nd number"))
if num1==num2==num3:
    print(" All are equal values")
elif num1>=num2 and num1>=num3:
    print(f"{num1} is largest value")    
elif num2>=num1 and num2>=num3:
    print(f"{num2} is largest value")        
else:
    print(f"{num3} is the largest value")