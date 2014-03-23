from solution import palindrom
import unittest

class TestIsIntPalindrom(unittest.TestCase):
	"""docstring for TestIsIntPalindrom"""
	def test_is_int_palindrom(self):
		self.assertEqual(True,palindrom(1))
		self.assertEqual(False,palindrom(42))
		self.assertEqual(True,palindrom(100001))
		self.assertEqual(True,palindrom(999))
		self.assertEqual(False,palindrom(123))

if __name__ == '__main__':
	unittest.main()