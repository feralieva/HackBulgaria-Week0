def sum_of_divisors(n):
	sum = 0
	iter = 1
	while iter <= n:
		if n%iter == 0:
			sum = sum + iter
		iter = iter + 1

	return sum

def is_prime(n):
	if sum_of_divisors(n) == 1 + n:
		return True
	return False

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