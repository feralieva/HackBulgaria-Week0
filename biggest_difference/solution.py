def biggest_difference(arr):
	diff = arr[0] - arr[1]
	iter = 1
	while iter <= len(arr) - 2:
		if (arr[iter] - arr[iter+1]) > diff:
			diff = arr[iter] - arr[iter+1]
		else:
			iter += 1
	return diff