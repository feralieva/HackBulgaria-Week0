import unittest
import solution
from subprocess import check_output

class TestGenerateNumbers(unittest.TestCase):
	"""docstring for TestGenerateNumbers"""
	def test_generate_numbers(self):
		numbers = check_output("py solution.py numbers.txt 3",shell=True).decode()
		check = check_output("cat numbers.txt",shell=True).decode()
		check = "%s\n"%(check.split())
		self.assertEqual(check,numbers)

if __name__ == '__main__':
	unittest.main()