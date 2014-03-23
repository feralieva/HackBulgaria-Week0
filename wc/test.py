import solution
import unittest
from subprocess import check_output

class TestWc(unittest.TestCase):
	"""docstring for TestWc"""
	def test_wc_words(self):
		words = check_output("py solution.py story.txt words",shell=True).decode()
		self.assertEqual('163\n',words)

	def test_wc_lines(self):
		lines = check_output("py solution.py story.txt lines",shell=True).decode()
		self.assertEqual('4\n',lines)

	def test_wc_chars(self):
		chars = check_output("py solution.py story.txt chars",shell=True).decode()
		self.assertEqual('1031\n',chars)

if __name__ == '__main__':
	unittest.main()