import numpy as np

def orthogonal_projection(v, L):
    koef = np.dot(v, L) / np.dot(L,L)
    
    return [koef * el for el in L]
