def count_consonants(str):
	consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
	count = 0

	for iter in str:
		for item in consonants:
			if iter == item:
				count = count + 1
	return count