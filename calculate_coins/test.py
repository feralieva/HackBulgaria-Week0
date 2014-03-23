import unittest
from solution import calculate_coins

class TestCalculateCoins(unittest.TestCase):
	"""docstring for TestCalculateCoins"""
	def test_calculate_coins(self):
		self.assertEqual({1: 1, 2: 1, 100: 0, 5: 0, 10: 0, 50: 1, 20: 0},calculate_coins(0.53))

if __name__ == '__main__':
	unittest.main()