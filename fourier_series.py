import numpy as np
from math import pi, sin, cos, sqrt, atan2
from mpl_widget import MplWidget

class FourierSeries:
    """
    Class for handling Fourier series visualization.
    """

    def __init__(self, safe_dict):
        """
        Initialize the FourierSeries object.
        """
        # Store safe_dict for mathematical expression evaluation
        self.safe_dict = safe_dict

    def evaluate_function(self, an, bn, n, t):
        """
        Evaluate the Fourier series function for a specific term.
        """
        # Evaluate expressions for an and bn
        an, bn = self._evaluate_expression(an, bn, n)

        # Calculate individual components of the Fourier series
        first = an * np.array(list(map(lambda x: cos(n * (2 * pi / self.period) * x), t)))
        second = bn * np.array(list(map(lambda x: sin(n * (2 * pi / self.period) * x), t)))

        # Calculate magnitude and phase angle
        magnitude = sqrt(an**2 + bn**2)
        theta = atan2(-1 * bn, an) * 180 / pi

        return first + second, magnitude, theta

    def find_values(self):
        """
        Find Fourier series values for all terms.
        """
        # Initialize data with a0 and time interval
        self.data[0, :] = self.data[0, :] + self.a0

        # Evaluate Fourier series for each term
        for n in range(1, self.limit_n + 1):
            element = n % self.mod_num
            value, mag, theta = self.evaluate_function(
                self.an_expression[element], self.bn_expression[element], n, self.time_interval
            )
            self.data[0] = self.data[0] + value

            # Store magnitude and phase angle for each term
            self.magnitude[0, n - 1] = mag
            self.theta[0, n - 1] = theta

        return self.data

    def _evaluate_expression(self, an, bn, n):
        """
        Evaluate mathematical expressions for an and bn using safe_dict.
        """
        self.safe_dict['n'] = n
        an_val = eval(an, {"__builtins__": None}, self.safe_dict)
        bn_val = eval(bn, {"__builtins__": None}, self.safe_dict)
        return an_val, bn_val
