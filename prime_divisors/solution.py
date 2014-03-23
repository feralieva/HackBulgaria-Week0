from is_prime import is_prime

def divisors(n):
	iter = 1
	dev = 0
	while iter <= n:
		if n%iter == 0:
			dev = dev + 1
		iter = iter + 1

	return dev

def prime_number_of_divisors(n):
	if is_prime(divisors(n)):
		return True
	return False
