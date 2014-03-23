def calculate_coins(sum):
	coins = [100, 50, 20, 10, 5, 2, 1]
	d = {}
	sum = int(sum * 100)
	for item in coins:
		if item in d:
			if sum >= item:
				sum = sum - item
				d[item] = d[item] + 1
		else:
			if sum >= item:
				sum = sum - item
				d[item] = 1
			else:
				d[item] = 0

	return d