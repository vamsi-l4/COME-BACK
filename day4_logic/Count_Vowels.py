text=input('enter the text: ')
count=0
for vowels in text:
    if vowels in 'aeiouAEIOU':
       count+=1
print(count)