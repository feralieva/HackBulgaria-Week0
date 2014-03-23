import sys

def sum_numbers(filename):
	file=open(filename,"r")
	contain = file.read()
	numbers = contain.split()
	sum = 0
	for i in numbers:
		sum += int(i)
	return sum

def main():
	print(sum_numbers(sys.argv[1]))

if __name__ == '__main__':
	main()