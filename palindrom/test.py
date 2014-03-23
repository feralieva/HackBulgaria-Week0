from solution import is_int_palindrom
import unittest

class TestIsIntPalindrom(unittest.TestCase):
	"""docstring for TestIsIntPalindrom"""
	def test_is_int_palindrom(self):
		self.assertEqual(True,is_int_palindrom(1))
		self.assertEqual(False,is_int_palindrom(42))
		self.assertEqual(True,is_int_palindrom(100001))
		self.assertEqual(True,is_int_palindrom(999))
		self.assertEqual(False,is_int_palindrom(123))

if __name__ == '__main__':
	unittest.main()