from random import random
from typing import Callable


def generate_points(f: Callable[[float], float], n: int, a: float, b: float,
                    random_space: bool = False, with_edges: bool = True,
                    add_noise: bool = False, noise_deviation: float = 1.0) -> list[tuple[float, float]]:
    points_y = [0.0] * n
    points_x = generate_x_axis(n, a, b, random_space, with_edges)
    if add_noise:
        for i in range(n):
            points_y[i] = f(points_x[i]) + noise_deviation * (random() - 0.5) * 2
    else:
        for i in range(n):
            points_y[i] = f(points_x[i])
    return list(zip(points_x, points_y))


def generate_x_axis(n: int, a: float, b: float,
                    random_space: bool = False, with_edges: bool = True) -> list[float]:
    result = [0.0] * n
    if random_space:
        for i in range(n):
            result[i] = a + random() * (b - a)
        result.sort()
    else:
        h = (b - a) / (n - 1)
        x = a
        for i in range(n):
            result[i] = x
            x += h
    if with_edges:
        result[0] = a
        result[-1] = b
    return result
