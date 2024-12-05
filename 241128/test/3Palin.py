def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

# 테스트
if __name__ == "__main__":
    a = "A man, a plan, a canal: Panama"
    print(is_palindrome(a))
