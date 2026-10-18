def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []

	match mode:
		case 'column':
			for col in range(len(matrix[0])):
				col_sum = 0
				for row in range(len(matrix)):
					col_sum += matrix[row][col]
				means.append(col_sum / len(matrix))
		case 'row':
			means = [sum(row) / len(row) for row in matrix]

	return means