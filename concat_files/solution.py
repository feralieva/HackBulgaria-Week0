import sys

def main():
	arr = []
	list_arg = list(sys.argv)
	filename = "MEGATRON.txt"
	file = open(filename,"a")
	for i in list_arg[1:]:
		file_name = i
		file1 = open(file_name,"r")
		content = file1.read()
		arr += [content]
	file.write("\n\n".join(arr))
	#print(arr)

if __name__ == '__main__':
	main()