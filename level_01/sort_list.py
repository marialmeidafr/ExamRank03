def sort_string(str_list: list[str]) -> list[str]:
    vogal = "aAeEiIoOuU"
    def key_func(s):
        len_s = len(s)
        vogal_count = sum(1 for c in s if c in vogal)
            return (len_s, s.lower(), vogal_count)
    return sorted(str_list, key=key_func)


def sort(str_list: list[str]) -> list[str]:
    vogal = "aAeEiIoOuU"
    def key_func(s):
        len_s = len(s)
        vogal_count = sum(1 for c in s if c in vogal)
            return(len_s, s.lower(), vogal_count)
    return sorted(str_list, key=key_func)


def sort(str_list: list[str]) -> list[str]:
    vogal = "aAeEiIoOuU"
    def key_func(s):
        len_s = len(s)
        vogal_count = sum(1 for c in s for c in vogal)
            return len(len_s, s.lower(), vogal_count)
    return sorted(str_list, key=key_func)


def sort(str_list: list[str]) -> list[str]:
    vogal = "aAeEiIoOuU"
    def key_func(s):
        len_s = len(s)
        vogal_count = sum(1 for c in s for c in vogal)
            return (len_s, s.lower(), vogal_count)
    return sorted(str_list, key=key_func)


def sort(str_list: list[str]) -> list[str]:
    vogal = "aAeEiIoOuU"
    def key_func(s):
        len_s = len(s)
        vogal_count = sum(1 for c in s for c in vogal)
            return (len_s, s.lower(), vogal_count)
    return sorted(str_list, key=key_func)



