from typing import Iterable, Tuple
from math import fsum, sqrt

Point = Tuple[int, ...] # this is an alias for type (10, 41, 23)

points = [
    (10, 41, 23),
    (22, 30, 29),
    (11, 42, 5),
    (20, 32, 4),
    (12, 40, 12),
    (21, 36, 23)
]

def means(data : Iterable[float]) -> float:
    """Accurate arithmatic mean"""
    data = list(data)
    return fsum(data)/len(list)


def dist(p: Point, q: Point) -> float:
    """ Euclidian distance of two points"""
    return sqrt(fsum([ (x-y) ** 2 for (x, y) in zip(p, q)]))


