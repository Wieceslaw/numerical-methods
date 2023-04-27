from typing import Callable


def euler_method(f: Callable[[float, float], float],
                 a: float, y_a: float, b: float, n: int = 1000) -> list[tuple[float, float]]:
    result = []
    dx = (b - a) / n
    x = a
    y = y_a
    for i in range(n):
        result.append((x, y))
        slope = f(x, y)
        x += dx
        y += dx * slope
    result.append((b, y))
    return result
