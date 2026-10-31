import numpy as np

operations = {
    'square': lambda x: x ** 2,
    'sin': np.sin,
    'exp': np.exp,
    'log': np.log,
    'cos': np.cos,
}

derivatives = {
    'square': lambda x: 2 * x,
    'sin': np.cos,
    'exp': np.exp,
    'cos': lambda x: -np.sin(x),
    'log': lambda x: 1 / x
    
}

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
    value = x
    gradient = 1.0

    for function in reversed(functions):
        gradient *= derivatives[function](value)
        value = operations[function](value)

    return gradient