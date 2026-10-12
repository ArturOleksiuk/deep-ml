def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
    if len(a) != len(b):
        return -1
        
    result = []
    
    for i in range(len(a)):
        sum = a[i] + b[i]
        result.append(sum)
        
    return result