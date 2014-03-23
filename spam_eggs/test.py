import unittest
from solution import prepare_meal

class TestSpamEggs(unittest.TestCase):
	"""docstring for TestSpamEggs"""
	def test_spam_and_eggs(self):
		self.assertEqual('spam',prepare_meal(3))
		self.assertEqual('spam spam spam',prepare_meal(27))
		self.assertEqual('',prepare_meal(7))
		self.assertEqual('eggs',prepare_meal(5))
		self.assertEqual('spam and eggs',prepare_meal(15))
		self.assertEqual('spam spam and eggs',prepare_meal(45))

if __name__ == '__main__':
	unittest.main()