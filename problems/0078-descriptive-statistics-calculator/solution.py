import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    result = {}
    
    result['mean'] = np.mean(data)
    result['median'] = np.median(data)

    frequency = {}

    for value in data:
        frequency[value] = frequency.get(value, 0) + 1

    result['mode'] = max(frequency, key=frequency.get)
    result['variance'] = np.var(data)
    result['standard_deviation'] = np.std(data)
    result['25th_percentile'] = np.percentile(data, 25)
    result['50th_percentile'] = np.percentile(data, 50)
    result['75th_percentile'] = np.percentile(data, 75)
    result['interquartile_range'] = result['75th_percentile'] - result['25th_percentile']

    return result
    