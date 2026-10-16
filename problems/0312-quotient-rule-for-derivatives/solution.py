import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    h_value = np.polyval(h_coeffs, x)

    if h_value == 0:
        raise ValueError("Denominator cannot be zero at x")
    
    g_value = np.polyval(g_coeffs, x)
    g_der_value = np.polyval(np.polyder(g_coeffs), x)
    h_der_value = np.polyval(np.polyder(h_coeffs), x)

    return ((g_der_value * h_value) - (g_value * h_der_value)) / h_value ** 2