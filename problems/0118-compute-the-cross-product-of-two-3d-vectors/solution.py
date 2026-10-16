import numpy as np

def cross_product(a: list, b: list) -> list:
    '''
    result = [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0] 
    ]

    return result
    '''
    return np.cross(a, b).tolist()