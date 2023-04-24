import math
import matplotlib.pyplot as plt

from approximation.methods.spline_interpolation import evaluate_spline
from lib.plot_gui import draw_function
from methods.cauchy_problem_solver import euler_method

if __name__ == '__main__':
    # f = lambda x, y: x * y * y
    # euler_points = euler_method(f, 0, 1, 1, 1000)
    # analytic_function = lambda x: 2 / (2 - x * x)
    # TODO: use interpolation

    # given
    equation = lambda x, y: -y * math.cos(x) + math.exp(-math.sin(x))
    n = 3
    a = 0
    b = 5
    y_a = 0

    # computation
    euler_points = euler_method(equation, a, b, y_a, n)
    euler_function_interpolation = evaluate_spline(euler_points)
    analytic_function = lambda x: x * math.exp(-math.sin(x))

    # plotting
    draw_function(euler_function_interpolation, a, b, label="euler", color="green")
    draw_function(analytic_function, 0, 5, label="analytic", color="red")
    plt.show()
