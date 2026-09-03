text=input("enter the text: ")
seen=set()
for ch in text:
    if ch in seen:
        print("1st repeated char: ",ch)
        break
    seen.add(ch)
else:
    print("Not enough repeated characters")
# #nth repeated char:
# #  text = input("Enter the text: ")
# n = int(input("Enter N: "))

# seen = set()
# repeated_count = 0

# for char in text:

#     if char in seen:
#         repeated_count += 1

#         if repeated_count == n:
#             print("Nth repeated character:", char)
#             break

#     else:
#         seen.add(char)
# else:
#     print("Not enough repeated characters")