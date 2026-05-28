def whisper_chiper(s: str, n: int) -> str:
    shift = ""
    for i in s:
        if 'a' <= i <= 'z':
            shift += chr((ord(i) + ord('a') + n) % 26 + ord('a'))
        elif 'A' <= i <= 'Z':
            shift += chr((ord(i) + ord('A') + n) % 26 + ord('A'))
        else:
            shift += i
    return shift
