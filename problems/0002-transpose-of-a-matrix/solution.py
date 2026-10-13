def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    if a is None or len(a) == 0 or len(a[0]) == 0:
        return []
    
    result = []

    for i in range(len(a[0])):
        row = []
        for j in range(len(a)):
            row.append(a[j][i])
        result.append(row)

    return result