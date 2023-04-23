from typing import Callable

import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.use("Qt5Agg")


def draw_function(f: Callable[[float], float],
                  lower_bound: float, upper_bound: float,
                  label: str = None, color: str = None,
                  n: int = 500) -> None:
    points = get_function_plot_points(f, lower_bound, upper_bound, n)
    plt.plot(*zip(*points), label=label, color=color)


def draw_point(x: float, y: float,
               label: str = None, color: str = "black", size: int = 10):
    plt.scatter([x], [y], color=color, s=size, zorder=5, label=label)


def draw_points(points: [tuple[float, float]],
                label: str = None, color: str = "black", size: int = 10):
    plt.scatter(*zip(*points), color=color, label=label, s=size, zorder=4)


def get_function_plot_points(f: Callable[[float], float],
                             lower_bound: float, upper_bound: float,
                             n: int) -> list[tuple[float, float]]:
    assert lower_bound <= upper_bound, "[Internal Error]: Lower bound must be lower or equal than upper bound"
    h = (upper_bound - lower_bound) / n
    x = [lower_bound + h * i for i in range(n)]
    y = [f(el) for el in x]
    return list(zip(x, y))
