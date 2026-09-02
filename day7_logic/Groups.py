groups={}
n=int(input("how many students: "))
for i in range(n):
    name=input("enter the name: ")
    language=input("enter the language: ")
    if language not in groups:
        groups[language]=[]
    groups[language].append(name)    
print(groups)        