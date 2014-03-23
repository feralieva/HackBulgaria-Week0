def count_words(arr):
	d = {}
	for item in arr:
		if item in d:   
			d[item] = d[item] + 1
		else:
			d[item] = 1


	return d