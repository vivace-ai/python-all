def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()     # 공백과 대소문자를 없앤다
    return cleaned == cleaned[::-1]


print(is_palindrome("기러기"))
print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("파이썬"))
