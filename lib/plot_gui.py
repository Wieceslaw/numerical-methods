from typing import Callable

import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.use("Qt5Agg")
plt.grid()
plt.legend()


def show_plot(
        control_points: list[tuple[float, float]],
        function_points: list[tuple[float, float]],
        spline_function_points: list[tuple[float, float]],
        function_str: str
):
    plt.scatter(*zip(*control_points), color="red", label="Control points", s=10)
    plt.plot(*zip(*function_points), label="Original function")
    plt.plot(*zip(*spline_function_points), color='green', label="Spline interpolation")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(f"Function: {function_str}")
    plt.show()


def get_function_plot_points(f: Callable[[float], float],
                             lower_bound: float, upper_bound: float,
                             n: int) -> list[tuple[float, float]]:
    assert lower_bound <= upper_bound, "[Internal Error]: Lower bound must be lower or equal than upper bound"
    h = (upper_bound - lower_bound) / n
    x = [lower_bound + h * i for i in range(n)]
    y = [f(el) for el in x]
    return list(zip(x, y))


def draw_function(f: Callable[[float], float],
                  lower_bound: float, upper_bound: float,
                  label: str = None, color: str = None,
                  n: int = 500) -> None:
    points = get_function_plot_points(f, lower_bound, upper_bound, n)
    plt.plot(*zip(*points), label=label, color=color)
