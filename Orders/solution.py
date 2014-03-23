from time import time
from datetime import datetime
import os
from subprocess import check_output
from glob import glob


def take(name, price, orders):
	if name in orders:
		orders[name] += price
	else:
		orders[name] = price
	return "Taking order from %s for %f"%(name, price)

def status(orders):
	result = []
	for i in orders:
		result.append("{} - {}".format(i, orders[i]))
	return result

def save(orders):
	ts = time()
	stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
	file_name = "orders_" + stamp
	file = open(file_name, "w")
	for i in orders:
		file.write("{} - {}\n".format(i, orders[i]))
	file.close()
	return file_name

def list():
	files = glob('orders_*')
	for i in range(len(files)):
		print("[{}] - {}".format(i+1, files[i]))
	return files

def load(order_files, number):
	file = open(order_files[number - 1], "r")
	content = file.read().splitlines()
	file.close()
	new_orders = {}
	for o in content:
		temp = o.split(' ')	
		new_orders[temp[0]] = float(temp[2])
	return new_orders



def command_menu():
	orders = {}
	order_files = []
	#d = {}
	is_saved_for_loading = True
	is_saved_for_finishing = True
	while True:
		command = input("Enter command>")
		command = command.split(' ')
		if command[0] == "take":
			is_saved_for_loading = False
			is_saved_for_finishing = False
			print('asd')
			take(command[1],float(command[2]),orders)
		elif command[0] == "status":
			print('\n'.join(status(orders)))
		elif command[0] == "save":
			is_saved_for_finishing = True
			is_saved_for_loading = True
			save(orders)
		elif command[0] == "list":
			order_files = list()
		elif command[0] == "load":
			if is_saved_for_loading == False:
				print("You have unsaved order.\nIf you wish to discard the current order, type load again\n")
				is_saved_for_loading = True
			else:
				orders.clear()
				orders = load(order_files, int(command[1]))
				is_saved_for_loading = True
				is_saved_for_finishing = True
		elif command[0] == "finish":
			if is_saved_for_finishing == False:
				print("You have not saved your order.\nIf you wish to continue, type finish again.\nf you want to save your order, type save\n")
				is_saved_for_finishing = True
			else:
				print("Finishing order. Goodbye!")
				break
		else:
			print("Unknowing command!\nTry one of the following:\ntake <name> <price>\nstatus\nsave\nlist\nload <number>\nfinish\n")
	

	

if __name__ == '__main__':
	command_menu()