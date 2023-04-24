import math
import matplotlib.pyplot as plt

from approximation.methods.spline_interpolation_solver import evaluate_spline
from lib.plot_gui import draw_function, draw_point
from lib.validated_read import read_int, read_float
from methods.cauchy_problem_solver import euler_method

functions = [
    (  # x: 0, y: 0
        (lambda x, y: -y * math.cos(x) + math.exp(-math.sin(x)), "y'(x) = -y * cos(x) + e^(sin(x))"),
        (lambda x: x * math.exp(-math.sin(x)), "y(x) = x * e^(-sin(x))")
    )
]


def main():
    # interactivity
    print("Equations:")
    for i in range(len(functions)):
        print(f"{i + 1}) {functions[i][0][1]}")
    f_num = read_int("Enter equation name", min_val=1, max_val=len(functions)) - 1
    (equation, equation_str), (analytical_solution_f, analytical_solution_f_str) = functions[f_num]

    # TODO: do I need initial_y and steps_num???
    initial_x = read_float("Enter initial condition argument")
    initial_y = read_float("Enter initial condition value")
    solution_x = read_float("Enter the point you are interested in", min_val=initial_x)
    steps_num = read_int("Enter number of steps", min_val=2)

    # computation
    euler_solution_points = euler_method(equation, initial_x, initial_y, solution_x, steps_num)
    euler_solution_f = evaluate_spline(euler_solution_points)
    solution_y = euler_solution_f(solution_x)
    print(f"Analytical solution: {analytical_solution_f_str}")

    # plotting
    draw_point(initial_x, initial_y, label="Initial condition", color="red")
    draw_point(solution_x, solution_y, label="Solution point", color="blue")
    draw_function(euler_solution_f, initial_x, solution_x, label="Euler solution", color="orange")
    draw_function(analytical_solution_f, initial_x, solution_x, label="Analytic solution", color="green")

    plt.title(equation_str)
    plt.grid()
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
