def count_substrings(haystack, needle):
	i = 0
	j = 0
	count = 0
	while i <= len(haystack) - 1:
		if haystack[i] == needle[j]:
			i = i + 1
			j = j + 1
			if j == len(needle):
				count = count + 1
				j = 0
		else:
				i = i + 1
				j = 0

	return count