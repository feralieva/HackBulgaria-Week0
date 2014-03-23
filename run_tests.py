from subprocess import check_output
from subprocess import call

def main():
	tests = check_output("find . -name test.py",shell=True).decode()
	tests = tests.split("\n")
	for s in tests:
		folder = s[:-7]
		call("cd {} && py test.py".format(folder),shell=True)

if __name__ == '__main__':
		main()	