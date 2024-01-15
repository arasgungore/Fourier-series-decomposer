from math import *

def create_safe_dict():
    """
    Create a dictionary with safe math functions for expression evaluation.
    """
    safe_list = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor',
                 'fmod', 'frexp', 'hypot', 'ldexp', 'log', 'log10', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh',
                 'sqrt', 'tan', 'tanh']

    safe_dict = {}
    for k in safe_list:
        safe_dict[k] = locals()[k]

    return safe_dict
