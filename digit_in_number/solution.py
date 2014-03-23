from palindrom import array_int

def contains_digit(number, digit):
	arr = array_int(number)
	for item in arr:
		if item == digit:
			return True
	return False