text=input("enter the text: ")
count={}
for char in text:
    if char in count:
        count[char]+=1
    else:
        count[char]=1
for char in count:
    if count[char]==1:
        print(char)            
        break 
# nth non repeating char
#text = input("Enter the text: ")
# n = int(input("Enter which non-repeating character: "))

# count = {}

# for char in text:
#     if char in count:
#         count[char] += 1
#     else:
#         count[char] = 1

# non_repeat_count = 0

# for char in text:
#     if count[char] == 1:
#         non_repeat_count += 1

#         if non_repeat_count == n:
#             print(char)
#             break
# else:
#     print("Not enough non-repeating characters") 