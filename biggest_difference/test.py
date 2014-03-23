from solution import biggest_difference
import unittest

class TestBiggestDifference(unittest.TestCase):
	def test_biggest_difference(self):
		self.assertEqual(-1,biggest_difference([1,2]))

if __name__ == '__main__':
	unittest.main()