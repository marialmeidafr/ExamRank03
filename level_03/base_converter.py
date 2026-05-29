def number_base_converter(num: str, src_base: int, dest_base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    try:
    	if not 2 <= from_base <= 36:
            return "ERROR"
        if not 2 <= to_base <= 36:
            return "ERROR"
        n = int(num, src_base)

        if n == 0:
            return "0"
        result = ""
        while n > 0:
            result = digits[n % dest_base] + result
            n //= dest_base
    except Exception:
        return "Error"
    return result
