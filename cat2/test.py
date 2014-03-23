from subprocess import check_output
import unittest
from solution import main

class TestCat2(unittest.TestCase):
	"""docstring for TestCat2"""
	def test_cat2(self):
		output = check_output("py cat2.py file1.txt file2.txt",shell=True).decode()
		self.assertEqual("Python is an awesome language!\nYou should try it.\n\n\n\nAlso, you can use Python at a lot of different places!\n\n\n\n",output)

if __name__ == '__main__':
	unittest.main()