from typing import Iterable, Tuple, Sequence, List, Dict
from math import fsum, sqrt
from collections import defaultdict
from functools import partial
from random import sample
from pprint import pprint

Point = Tuple[int, ...] # this is an alias for type (10, 41, 23)
Centroid = Point



def mean(data : Iterable[float]) -> float:
    """Accurate arithmatic mean"""
    data = list(data)
    return fsum(data)/len(data)


def dist(p: Point, q: Point) -> float:
    """ Euclidian distance of two points"""
    return sqrt(fsum([ (x-y) ** 2 for (x, y) in zip(p, q)]))


def assign_data(centroids: Sequence[Centroid], data: Iterable[Point]) ->Dict[Centroid, List[Point]] :
    """Group the data points closest to centroid"""
    d = defaultdict(list)
    for point in data:
        closest_centroid = min(centroids, key=partial(dist, point))
        d[closest_centroid].append(point)
    return dict(d)


def compute_centroids(groups):
    """compute the centroid of each group"""
    return [tuple(map(mean, zip(*group))) for group in groups]


def k_means(data, k=2, iterations=50):
    data = list(data)
    centroids = sample(data, k)
    for i in range(iterations):
        labeled = assign_data(centroids, data)
        centroids = compute_centroids(labeled.values())
    return centroids


if __name__ == '__main__':
    points = [
        (10, 41, 23),
        (22, 30, 29),
        (11, 42, 5),
        (20, 32, 4),
        (12, 40, 12),
        (21, 36, 23)
    ]
    centroids = k_means(points)
    groups = assign_data(centroids, points)
    pprint(groups)