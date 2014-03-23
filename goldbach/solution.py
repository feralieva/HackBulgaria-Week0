from is_prime import is_prime

def goldbach(n):
	i = 1
	arr = []
	while i <= n/2:
		if is_prime(i) and is_prime(n-i):
			arr = arr + [(i, n-i)]
			i += 1
		else:
			i += 1
	return arr