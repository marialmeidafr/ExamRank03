def():
    if len(new_s) != len(new_t):
        return False
    return sorted(new_s) == sorted(new_t)
