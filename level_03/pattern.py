def pattern_tracker(s: str) -> int:
    count = 0
    for i in range(len(s) - 1):
        if s[i].isdigit() and s[i+1].isdigit() and s[i+1] > s[i] and int(s[i+1]) == int(s[i] + 1):
                count += 1
    return count
