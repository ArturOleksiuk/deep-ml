import numpy as np

def cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
    if v1.ndim != 1 or v2.ndim != 1:
        raise ValueError("Both inputs must be 1D arrays")
    
    if v1.shape != v2.shape:
        raise ValueError("Vectors must be the same shape")

    if v1.size == 0:
        raise ValueError("Vectors cannot be empty")
    
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    
    if norm_v1 == 0 or norm_v2 == 0:
        raise ValueError("Vectors cannot have zero magnitude")

    return float(np.dot(v1, v2) / (norm_v1 * norm_v2))