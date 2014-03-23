def gcd(a,b):
	while b != 0:
		(a, b) = (b, a%b)
	return a

def simplify_fraction(fraction):
	digit = list(fraction)
	g = gcd(digit[0], digit[1])
	digit[0] = digit[0]//g
	digit[1] = digit[1]//g
	fraction = tuple(digit)
	return fraction