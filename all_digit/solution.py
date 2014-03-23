from digit_in_number import contains_digit

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
