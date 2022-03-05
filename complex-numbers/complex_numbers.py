"""
    Complex number exercise
"""

from math import sqrt, cos, sin, e

class ComplexNumber:
    """
        Define math operations for Complex Number
    """
    def __init__(self, real, imaginary):
        self.real, self.imaginary = real, imaginary

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNumber(other, 0)
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNumber(other, 0)
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return ComplexNumber(real, imaginary)

    __radd__ = __add__

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNumber(other, 0)
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNumber(real, imaginary)

    __rmul__ = __mul__

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNumber(other, 0)
        real = self.real - other.real
        imaginary = self.imaginary - other.imaginary
        return ComplexNumber(real, imaginary)

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNumber(other, 0)
        return other - ComplexNumber(self.real, self.imaginary)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNumber(other, 0)
        real = self.real * other.real + self.imaginary * other.imaginary
        real /= other.real ** 2 + other.imaginary ** 2
        imaginary = self.imaginary * other.real - self.real * other.imaginary
        imaginary /= other.real ** 2 + other.imaginary ** 2
        return ComplexNumber(real, imaginary)

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNumber(other, 0)
        return other / ComplexNumber(self.real, self.imaginary)

    def __abs__(self):
        return sqrt(self.real ** 2 + self.imaginary ** 2)

    def conjugate(self):
        """
            Return the conjugate of a complext number
        """
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        """
            Raising e to a complex exponent
        """
        result = e ** self.real * ComplexNumber(cos(self.imaginary), sin(self.imaginary))
        return result
