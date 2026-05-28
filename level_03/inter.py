def inter():
    res = ""
    for char in s1:
        if char in s2 and char not in res:
            res += char
    return res
