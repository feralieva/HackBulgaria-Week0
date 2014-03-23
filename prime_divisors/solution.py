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
