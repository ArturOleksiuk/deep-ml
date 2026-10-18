import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	rows, cols = new_shape

	if (rows * cols) == (len(a) * len(a[0])): 
		return np.array(a).reshape(new_shape).tolist()
	
	return []
	