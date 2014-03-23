def list_to_number(digits):
	iter = len(digits) - 1
	pow = 0
	numb = 0
	while iter >= 0:
		numb = numb + (digits[iter]*(10 ** pow))
		pow = pow + 1
		iter = iter - 1
	return numb