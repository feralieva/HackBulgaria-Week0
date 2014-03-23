import unittest
import solution
import os

class TestPizza(unittest.TestCase):
	"""docstring for TestPizza"""
	def test_pizza_take(self):
		orders = {}
		solution.take("yoana", 15.0, orders)
		self.assertEqual({"yoana": 15.0}, orders)

	def test_pizza_status(self):
		orders = {"peio": 13.0, "katq": 14.0}
		exp = ["peio - 13.0", "katq - 14.0"]
		self.assertEqual(exp, solution.status(orders))

	def test_save(self):
		orders = {"peio": 13.0, "katq": 14.0}
		output = solution.save(orders)
		file = open(output,"r")
		content = sorted(file.read().splitlines())
		file.close()
		os.remove(output)
		exp = ["katq - 14.0", "peio - 13.0"]
		self.assertEqual(exp,content)


		#self.assertEqual("Taking order from Niki for 15.000000",pizza.command_menu("Niki",15.000000,{}))
		#self.assertEqual("Niki - 15.000000\nYoanna - 35.000000",pizza.command_menue7({"Niki": 25.000000, "Yoanna": 35.000000}))
		#self.assertEqual("You have unsaved order.\nIf you wish to discard the current order, type load again\n",pizza.load(1))
		#self.assertEqual("",pizza.list())
		#self.assertEqual(",pizza.load(1)")
		#self.assertEqual("Taking order from John for 35.000000",pizza.command_menu("take", "John",35.000000,{}))
		#self.assertEqual("You have not saved your order.\nIf you wish to continue, type finish again.\nIf you want to save your order, type save\n",pizza.command_menu("finish"))
		#self.assertEqual("Finishing order. Goodbye!",pizza.command_menu("finish"))

		

if __name__ == '__main__':
	unittest.main()