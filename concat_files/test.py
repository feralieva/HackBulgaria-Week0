import unittest
import solution
from subprocess import call
from subprocess import check_output

class TestConcatFiles(unittest.TestCase):
	"""docstring for TestConcatFiles"""
	def test_concat_files(self):
		concat = call("py solution.py file1.txt file2.txt",shell=True)
		check_concat = check_output("cat MEGATRON.txt",shell=True).decode()
		self.assertEqual('Python is an awesome language!\nYou should try it.\n\nAlso, you can use Python at a lot of different places!',check_concat)
if __name__ == '__main__':
	unittest.main()