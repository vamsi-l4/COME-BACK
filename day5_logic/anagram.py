text1 = input("enter the text1: ")
text2= input("enter the text2: ")
count1 = {}
count2 = {}
for char in text1:
    if char in count1:
        count1[char] += 1
    else:
        count1[char] = 1
for char in text2:
    if char in count2:
        count2[char]+=1
    else:
        count2[char]=1
if count1==count2:
    print("anagram")                    
else:
    print("not anagram")
# another way
# text1 = input()
# text2 = input()

# if sorted(text1) == sorted(text2):
#     print("Valid Anagram")
# else:
#     print("Not Anagram")