def reverse_string(n):
    if n=="":
        return ""
    return reverse_string(n[1:])+n[0]
n=input("enter text: ")
print(reverse_string(n))