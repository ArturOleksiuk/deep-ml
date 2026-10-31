import math
import numpy as np

NUMBER_DAY = 15

def power_grid_forecast(consumption_data): 
    adjusted_data = [
        el - 10 * math.sin(2 * math.pi * (i + 1) / 10) 
        for i, el in enumerate(consumption_data)
    ]

    days = [i + 1 for i in range(len(consumption_data))]

    X = np.column_stack((
        np.ones(len(consumption_data)),
        np.array(days)
    ))

    theta = np.linalg.solve(X.T @ X, X.T @ adjusted_data)

    prediction = theta[0] + theta[1] * NUMBER_DAY;
    fluctuation = 10 * math.sin(2 * math.pi * NUMBER_DAY / 10)
    
    return math.ceil((prediction + fluctuation) * 1.05)