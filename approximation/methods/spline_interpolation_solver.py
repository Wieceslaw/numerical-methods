from typing import Callable

from linear.methods.gauss_solver import gauss_elimination


def evaluate_spline(points: list[tuple[float, float]]) -> Callable[[float], float]:
    x, y = zip(*points)
    n = len(points)
    h = calc_h(x)
    f = calc_constant_column(y, h)
    matrix = calc_coefficient_matrix(h)
    c = gauss_elimination(matrix, f)
    c = [0.0] + c + [0.0]
    a = y[1:]
    d = calc_d(h, c)
    b = calc_b(h, d, y, c)
    c = c[1:]
    spline_segments = [evaluate_spline_segment_function(x, i, a, b, c, d) for i in range(n - 1)]
    function = combine_spline_segments(spline_segments, x)
    return function


def combine_spline_segments(spline_segments: list[Callable[[float], float]],
                            intervals: list[float]):
    def f(x: float):
        i = find_interval(intervals, x)
        return spline_segments[i](x)

    return f


def find_interval(interval_parts: list[float], x: float) -> int:
    for i in range(0, len(interval_parts) - 1):
        if interval_parts[i] <= x <= interval_parts[i + 1]:
            return i
    raise IndexError("Out of bound")


def evaluate_spline_segment_function(
        intervals: list[float],
        index: int,
        a: list[float],
        b: list[float],
        c: list[float],
        d: list[float]
):
    def f(x: float) -> float:
        dx = x - intervals[index + 1]
        return a[index] + (b[index] * dx) + ((c[index] / 2) * dx * dx) + ((d[index] / 6) * dx * dx * dx)

    return f


def calc_coefficient_matrix(h: list[float]) -> list[list[float]]:
    n = len(h) + 1
    matrix = [[0.0 for _ in range(n - 2)] for _ in range(n - 2)]
    for i in range(n - 2):
        a = h[i]
        b = h[i + 1]
        c = 2 * (h[i] + h[i + 1])
        matrix[i][i] = c
        if i < n - 3:
            matrix[i][i + 1] = b
        if i > 0:
            matrix[i][i - 1] = a
    return matrix


def calc_constant_column(f: list[float], h: list[float]) -> list[float]:
    result = []
    n = len(f)
    for i in range(1, n - 1):
        result.append(6 * (((f[i + 1] - f[i]) / h[i]) - ((f[i] - f[i - 1]) / h[i - 1])))
    return result


def calc_h(x: list[float]) -> list[float]:
    return [x[i + 1] - x[i] for i in range(len(x) - 1)]


def calc_d(h: list[float], c: list[float]) -> list[float]:
    n = len(c)
    d = [0.0] * (n - 1)
    for i in range(n - 1):
        d[i] = (c[i + 1] - c[i]) / h[i]
    return d


def calc_b(h: list[float], d: list[float], f: list[float], c: list[float]) -> list[float]:
    n = len(f)
    b = [0.0] * (n - 1)
    for i in range(n - 1):
        b[i] = ((1 / 2) * h[i] * c[i + 1]) - ((1 / 6) * h[i] * h[i] * d[i]) + ((f[i + 1] - f[i]) / h[i])
    return b
