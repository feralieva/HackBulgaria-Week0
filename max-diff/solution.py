def biggest_difference(arr):
	array = []
	i = 1
	while i <= len(arr) - 1:
		array = array + [arr[i]]
		i = i + 1
	min = arr[0] - array[0]

	for iter in arr:
		for item in array:
			if (iter - item) < min:
				min = iter - item
			if item - iter < min:
				min = item - iter
	return min

def main():
	print(biggest_difference([-10, -9, -1]))
	print(biggest_difference(range(100)))
	print(biggest_difference([3,1,2]))
	print(biggest_difference([1,2,3,4,5]))

if __name__ == '__main__':
	main()