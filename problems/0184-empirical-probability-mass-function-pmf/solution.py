def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    frequences = {}

    for el in samples:
        frequences[el] = frequences.get(el, 0) + 1

    return [(key, frequences[key] / len(samples)) for key in frequences]
