def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0]!=text[len(text)-1]:
        return False
    return is_palindrome(text[1:len(text)-1])

text=input("enter text: ")
print(is_palindrome(text))