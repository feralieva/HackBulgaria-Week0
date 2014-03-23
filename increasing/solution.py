def is_increasing(seq):
	iter = 0
	while iter <= len(seq) - 2:
		if seq[iter] >= seq[iter + 1]:
			return False
		else:
			iter = iter + 1
	return True