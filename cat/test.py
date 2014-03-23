import unittest
import sys
from subprocess import check_output
from solution import main

class TestCat(unittest.TestCase):
	"""docstring for TestCat"""
	def test_cat(self):
		output = check_output('py cat.py file.txt', shell=True).decode()
		self.assertEqual("Python is an awesome language!\nYou should try it.\n", output)

if __name__ == '__main__':
	unittest.main()