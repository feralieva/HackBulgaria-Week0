def sum_of_min_and_max(arr):
	min = arr[0]
	max = arr[0]

	for item in arr:
		if item < min:
			min = item
		if item > max:
			max = item

	sum = min + max
	return sum