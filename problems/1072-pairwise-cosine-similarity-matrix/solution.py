import numpy as np

def pairwise_cosine_similarity(X):
    norms = [np.linalg.norm(row, ord=2) for row in X]

    matrix = np.zeros((len(X), len(X)))

    for i in range(len(X)):
        for j in range(len(X)):
            if norms[i] == 0 or norms[j] == 0:
                matrix[i][j] = 0.0
            else:
                matrix[i][j] = np.dot(X[i], X[j]) / (norms[i] * norms[j])

    return np.round(matrix, 4).tolist()