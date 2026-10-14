def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]] | int:
    if not a or not b:
        return []
    
    if len(a[0]) != len(b):
        return -1
    
    result = []
    
    for i in range(len(a)):

        row = []
        
        for j in range(len(b[0])):
            current_sum = 0

            for k in range(len(b)):
                current_sum += a[i][k] * b[k][j]
                
            row.append(current_sum)
            
        result.append(row)

    return result