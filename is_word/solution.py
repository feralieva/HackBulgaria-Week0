def is_an_bn(word):
	iter = 0
	if len(word)%2 != 0:
		return False
	else:
		while iter <= len(word)/2 - 1:
			if word[iter] != "a":
				return False
			else:
				iter = iter + 1
		while iter <=len(word) - 1:
			if word[iter] != "b":
				return False
			else:
				iter = iter + 1
		return True