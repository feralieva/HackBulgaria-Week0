def groupby(func, seq):

	d = {}
	for item in seq:
		if func(item) in d:
			d[func(item)] = d[func(item)] + [item]
		else:
			d[func(item)] = [item]

	return d