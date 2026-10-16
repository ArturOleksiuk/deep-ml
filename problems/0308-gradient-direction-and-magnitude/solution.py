import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
    result = {}

    result['magnitude'] = np.linalg.norm(np.array(gradient), ord=2)

    if result['magnitude'] == 0:
        result['direction'] = [0.0 for el in gradient]
        result['descent_direction'] = [0.0 for el in gradient]
    else: 
        result['direction'] = [el / result['magnitude'] for el in gradient]
        result['descent_direction'] = [-el for el in result['direction']]

    return result