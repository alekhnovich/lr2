def is_palindrome(text):
    text = text.lower()
    text = text.replace(' ', '')
    return text == text[::-1]


print(is_palindrome("топот"))
print(is_palindrome("привет"))
print(is_palindrome('А роза упала на лапу Азора'))
