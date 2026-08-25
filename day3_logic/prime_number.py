n=int(input('enter a number: '))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count ==2:
    print('prime')
else:
    print('not prime')        
n=int(input('enter a number: '))
if n<2:
    print('not prime')
else:
    for i in range(2,n):
        if n%i==0:
            print('not prime')    
            break
    else:
        print('prime')