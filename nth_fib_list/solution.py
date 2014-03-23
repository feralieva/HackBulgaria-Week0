def nth_fib_lists(listA, listB, n):
	index=3
	arr = []
	if n == 1 :
		return listA
	if n == 2 :
		return listB

	while index <= n:
		arr = listA + listB
		listA = listB
		listB = arr
		index = index + 1

	return arr