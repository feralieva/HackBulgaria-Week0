def sevens_in_a_row(arr, n):
	sevens = 0
	is_sevens = False
	for item in arr:
		if item == 7:
			sevens = sevens + 1
		else:
			if n == sevens:
				is_sevens = True
				return True
			sevens = 0
	return is_sevens
