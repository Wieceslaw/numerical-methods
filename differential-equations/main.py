import math
import matplotlib.pyplot as plt

from lib.plot_gui import draw_function
from methods.cauchy_problem_solver import euler_method

if __name__ == '__main__':
    # f = lambda x, y: x * y * y
    # euler_points = euler_method(f, 0, 1, 1, 1000)
    # analytic_function = lambda x: 2 / (2 - x * x)

    f = lambda x, y: -y * math.cos(x) + math.exp(-math.sin(x))
    euler_points = euler_method(f, 0, 5, 0, 100)
    analytic_function = lambda x: x * math.exp(-math.sin(x))

    plt.plot(*zip(*euler_points), label="euler", color="green")
    draw_function(analytic_function, 0, 5, label="analytic", color="red")
    plt.show()
