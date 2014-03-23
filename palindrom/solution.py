def array_int(n):
	arr = []
	while n!=0:
		arr = arr + [n%10]
		n = n // 10
	return arr

def palindrom(n):
	arr = array_int(n)
	length = len(arr)
	iter_start =0
	iter_end = length - 1

	while iter_start < iter_end:
		if arr[iter_start] == arr[iter_end]:
			iter_start = iter_start + 1
			iter_end = iter_end -1
		else:
			return False
	return True
