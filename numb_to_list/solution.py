def number_to_list(n):
	arr = []
	while n != 0:
		arr = arr + [n%10]
		n = n // 10

	arr_new = []
	iter = 0
	new_iter = len(arr) - 1
	while iter <= len(arr) - 1:
		arr_new = arr_new + [arr[new_iter]]
		iter = iter + 1
		new_iter = new_iter - 1
	return arr_new