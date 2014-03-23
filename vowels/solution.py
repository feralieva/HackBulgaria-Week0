def count_vowels(str):
	vow = "aeiouyAEIOUY"
	count = 0

	for item in str:
		for iter in vow:
			if iter == item:
				count = count + 1

	return count