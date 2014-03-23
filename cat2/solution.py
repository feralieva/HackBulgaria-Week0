import sys

def main():
	list_files = sys.argv[1:]
	for i in list_files:
		filename = i
		file = open(filename,"r")
		content = file.read()
		print(content)
		print("\n\n")

if __name__ == '__main__':
    main()