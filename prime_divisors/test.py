from solution import prime_number_of_divisors
import unittest

class TestPrimeNumberOfDivisors(unittest.TestCase):
	"""docstring for TestPrimeNumberOfDivisors"""
	def test_prime_numb_of_div(self):
		self.assertEqual(True,prime_number_of_divisors(7))
		self.assertEqual(False,prime_number_of_divisors(8))
		self.assertEqual(True,prime_number_of_divisors(9))

if __name__ == '__main__':
	unittest.main()