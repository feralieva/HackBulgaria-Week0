def prepare_meal(number):
	arr = ''
	if number % 3 != 0:
		if number % 5 == 0:
			return 'eggs'
		else:
			return arr
	else:
		while number % 3 == 0:
			number = number//3
			arr = arr + 'spam'
			if number % 3 == 0:
				arr += ' '
		if number % 5 != 0:
			return arr
		else:
			arr += ' and eggs'

	return arr