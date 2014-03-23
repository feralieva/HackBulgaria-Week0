import sys
from random import randint

def main():
	arr = []
	filename = sys.argv[1]
	n = int(sys.argv[2])
	file = open(filename,"w")
	for i in range(0,n):
		p = randint(1,1000)
		arr+= [str(p)]
	file.write(" ".join(arr))
	print(arr)

if __name__ == '__main__':
    main()