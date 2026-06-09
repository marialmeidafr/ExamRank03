def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    list1 = list1 or []
    list2 = list2 or []

    mixed = list1 + list2
    mixed.sort()
    return mixed
