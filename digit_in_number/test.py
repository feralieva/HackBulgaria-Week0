from solution import contains_digit
import unittest

class TestContainsDigit(unittest.TestCase):
	"""docstring for TestContainsDigit"""
	def test_contains_digit(self):
		self.assertEqual(False,contains_digit(123,4))
		self.assertEqual(True,contains_digit(42,2))
		self.assertEqual(True,contains_digit(1000,0))
		self.assertEqual(False,contains_digit(12346789, 5))

if __name__ == '__main__':
	unittest.main()