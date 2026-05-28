def string_sculptor(text: str) -> str:
    res = ""
    count = 0
    for char in text:
        if char.isalpha():
            if count % 2 == 0:
                res += char.lower()
            else:
                res += char.upper()
            count += 1
        else:
            res += char
    return res
