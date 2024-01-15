from math import acos, asin, atan, atan2, ceil, cos, cosh, degrees, e, exp, fabs, floor, fmod, frexp, hypot, ldexp, log, log10, modf, pi, pow, radians, sin, sinh, sqrt, tan, tanh

def create_safe_dict():
    """
    Create a dictionary containing safe mathematical functions.
    """
    safe_dict = {
        'acos': acos, 'asin': asin, 'atan': atan, 'atan2': atan2, 'ceil': ceil, 'cos': cos,
        'cosh': cosh, 'degrees': degrees, 'e': e, 'exp': exp, 'fabs': fabs, 'floor': floor,
        'fmod': fmod, 'frexp': frexp, 'hypot': hypot, 'ldexp': ldexp, 'log': log, 'log10': log10,
        'modf': modf, 'pi': pi, 'pow': pow, 'radians': radians, 'sin': sin, 'sinh': sinh, 'sqrt': sqrt,
        'tan': tan, 'tanh': tanh
    }

    return safe_dict
