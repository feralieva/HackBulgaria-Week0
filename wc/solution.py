import sys

def wc(filename, command):
	file = open(filename, "r")
	content = file.read()
	count_char = 0
	count_words = 0
	count_lines = 0
	for i in content:
		count_char += 1
		if(i == " "):
			count_words += 1
		if(i == "\n"):
			count_lines += 1
	if(command == "chars"):
		return count_char
	if(command == "words"):
		return count_words
	if(command == "lines"):
		return count_lines


def main():
	print(wc(sys.argv[1], sys.argv[2]))

if __name__ == '__main__':
	main()