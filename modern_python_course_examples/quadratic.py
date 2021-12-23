import math
from typing import Tuple

def quadratic(a: float, b: float, c: float) -> Tuple[float, float]:
    """ Compute the two roots of the quadratic equation:
        ax^2 + bx + c = 0
        written in python as:
        a*x**2 + b*x + c = 0
        for example:
        >>> x1, x2 = quadratic(a=8, b=22, c=15)
        >>> x1
        -1.25
        >>> x2
        -1.5
        >>> 8*x1**2.0 + 22*x1 + 15
        0.0
        >>> 8*x2**2.0 + 22*x2 + 15
        0.0

    """
    discriminant = math.sqrt(b**2.0 - 4.0*a*c)
    x1 = (-b + discriminant) / (2.0 * a)
    x2 = (-b - discriminant) / (2.0 * a)
    return x1, x2


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())