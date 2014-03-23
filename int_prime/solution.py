from is_prime import is_prime

def prime_factorization(n):
	arr = []
	pow = 0
	numb = 2
	while n != 1:
		if is_prime(numb):
			if n % numb == 0:
				while n % numb == 0:
					pow = pow + 1
					n = n//numb
				arr = arr + [(numb, pow)]
				numb = numb + 1
				pow = 0
			else:
				numb =numb  + 1
		else:
			numb = numb + 1
	return arr