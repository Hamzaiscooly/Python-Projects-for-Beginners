# palindrome.py
# Check if a word or phrase is a palindrome

def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]

word = input("Enter a word or phrase: ")
if is_palindrome(word):
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is not a palindrome.")
