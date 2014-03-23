import unittest
import sys
from subprocess import check_output
from solution import main

class TestCat(unittest.TestCase):
	"""docstring for TestCat"""
	def test_cat(self):
		output = check_output('cat file.txt', shell=True).decode()
		self.assertEqual("Python is an awesome language!\nYou should try it.", output)

if __name__ == '__main__':
	unittest.main()