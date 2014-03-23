import unittest
from solution import sum_numbers
from subprocess import check_output

class TestSumNumbers(unittest.TestCase):
	"""docstring for TestSumNumbers"""
	def test_sum_numbers(self):
		check = check_output("py solution.py numbers.txt",shell=True).decode()
		self.assertEqual("1087\n",check)

if __name__ == '__main__':
	unittest.main()