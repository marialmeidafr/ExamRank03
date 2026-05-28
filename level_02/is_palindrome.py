def is_palindrome(s: str) -> bool:
    if s == "":
        return False
    else:
        clean = ''.join(char.lower() for char in s if char.isalnum())
    return clean == clean[::-1]

