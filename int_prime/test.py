from solution import prime_factorization
import unittest

class TestIntPrime(unittest.TestCase):
	"""docstring for TestIntPrime"""
	def test_int_prime_factorization(self):
		self.assertEqual([(2, 1), (5, 1)],prime_factorization(10))
		self.assertEqual([(2, 1), (7, 1)],prime_factorization(14))
		self.assertEqual([(2, 2), (89, 1)],prime_factorization(356))
		self.assertEqual([(89, 1)],prime_factorization(89))
		self.assertEqual([(2, 3), (5, 3)],prime_factorization(1000))

if __name__ == '__main__':
	unittest.main()