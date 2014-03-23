def magic_square(matrix):
	i = 1
	suma = sum(matrix[0])
	while i <= len(matrix)-1:
		if sum(matrix[i]) != suma:
			return False
		else:
			i += 1
	
	i = 0
	j = 0
	sum_col = 0
	list_sum = []
	while j <= len(matrix)-1:
		while i <= len(matrix)-1:
			sum_col += matrix[i][j]
			i += 1
		list_sum += [sum_col]
		sum_col = 0
		j += 1
		i = 0
	r = 1

	#col = sum([row[i] for row in matrix])

	sum_col = list_sum[0]
	while r <= len(list_sum)-1:
		if list_sum[r] != sum_col:
			return False
		else:
			r += 1

	if suma != sum_col:
		return False

	i = 0
	j = 0
	sum_diag1 = 0
	while i <= len(matrix)-1:
		while j <= i:
			if i == j:
				sum_diag1 += matrix[i][j]
				j += 1
			else:
				j += 1
		i += 1

	i = 0
	j = len(matrix)-1
	sum_diag2 = 0
	while j >= 0:
		sum_diag2 += matrix[i][j]
		i += 1
		j -= 1

	if sum_diag2 != sum_diag1:
		return False
	else:
		if sum_diag1 == suma:
			return True
		else:
			return False
			
