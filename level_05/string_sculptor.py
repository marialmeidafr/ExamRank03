def sculptor(text: str) -> str:
	result = ""
	count = 0
	p = True
	while count < len(text):
		if text[count].isalpha():
			if p:
				result += text[count].lower()
			else:
				result += text[count].upper()
			p = not p
		else:
			result += text[count]
		count += 1
	return result
