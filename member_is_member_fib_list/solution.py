def nth_fib_lists(listA, listB, n):
	if n == 1:
		return listA
	if n == 2:
		return listB
	index=3

	while index <= n:
		next = listA + listB
		listA = listB
		listB = next
		index = index + 1

	return listB