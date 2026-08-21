n= int(input('enter a number: '))
reverse_number=0
while n!=0:
    digit=n%10
    reverse_number=reverse_number*10+digit
    n//=10
print(reverse_number)        
