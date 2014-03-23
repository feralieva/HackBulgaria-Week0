def array_int(n):
	arr = []
	while n!=0:
		arr = arr + [n%10]
		n = n // 10
	return arr

def contains_digit(number, digit):
	arr = array_int(number)
	for item in arr:
		if item == digit:
			return True
	return False

def contains_digits(number, digits):
	iter = 0
	if digits == []:
		return True
	while iter != len(digits):
		if contains_digit(number, digits[iter]):
			iter = iter + 1
		else:
			return False
	return True
