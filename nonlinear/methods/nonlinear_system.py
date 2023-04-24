from typing import Callable

from linear.methods.gauss_solver import gauss_elimination


def compute_partial_derivative(f: Callable[[list[float]], float],
                               i: int) -> Callable[[list[float]], float]:
    def function(x: list[float]) -> float:
        d = 1e-6
        dx = x[::]
        dx[i] += d
        return (f(dx) - f(x)) / d

    return function


def compute_jacobian(functions: list[Callable[[list[float]], float]],
                     n: int):
    matrix = []
    for i in range(len(functions)):
        row = [compute_partial_derivative(functions[i], j) for j in range(n)]
        matrix.append(row)
    return matrix


def newton_method(system: list[Callable[[list[float]], float]],
                  e: float, max_i: int = 1000) -> list[float]:
    n = len(system)
    jacobian = compute_jacobian(system, n)
    x = [0] * n
    s = 10 * e
    i = 0
    while i < max_i and s > e:
        i += 1
        a = [[df(x) for df in row] for row in jacobian]
        b = [-f(x) for f in system]
        dx = gauss_elimination(a, b)
        s = abs(max(dx, key=abs))
        x = [x[i] + dx[i] for i in range(n)]
    return x
