from all_divisors import sum_of_divisors

def is_prime(n):
	if sum_of_divisors(n) == 1 + n:
		return True
	return False