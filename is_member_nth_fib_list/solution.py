def member_of_nth_fib_lists(listA, listB, needle):
	while len(listA) + len(listB) <= len(needle):
		if needle == listA + listB:
			return True
		else:
			next = listA + listB
			listA = listB
			listB = next
	return False