from typing import Callable


def middle_rule(start_point: float, dx: float, iteration: int) -> float:
    return start_point + dx / 2 + iteration * dx


def left_rule(start_point: float, dx: float, iteration: int) -> float:
    return start_point + iteration * dx


def right_rule(start_point: float, dx: float, iteration: int) -> float:
    return start_point + (iteration + 1) * dx


def integrate_with_rule(
        function: Callable[[float], float], rule: Callable[[float, float, int], float],
        lower_bound: float, upper_bound: float, n: int
) -> float:
    sm = 0
    dx = (upper_bound - lower_bound) / n
    for i in range(n):
        sm += function(rule(lower_bound, dx, i))
    return sm * dx


def rectangular_integration(
        function: Callable[[float], float],
        integration_rule: Callable[[float, float, int], float],
        lower_bound: float, upper_bound: float, runge_coeff: float = 1,
        epsilon: float = 1e-6, max_iter: int = 1000,
        start_iter: int = 2, reverse: bool = False
) -> tuple[float, float]:
    n = start_iter
    result = 0.0
    error = 0.0
    for _ in range(max_iter):
        tmp = integrate_with_rule(function, integration_rule, lower_bound, upper_bound, n)
        error = abs(result - tmp)
        if error * runge_coeff < epsilon:
            break
        result = tmp
        n *= 2
    if reverse:
        return -1 * result, error
    return result, error
