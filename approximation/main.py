import math
import matplotlib.pyplot as plt

from approximation.methods.points_generation import generate_points
from lib.plot_gui import draw_function, draw_points, draw_point
from lib.validated_read import read_int, read_string, read_float
from methods.spline_interpolation import evaluate_spline

functions = [
    (lambda x: math.log(x), "f(x) = log(x)"),
    (lambda x: math.sin(x), "f(x) = sin(x)"),
]


def is_valid_interval(f_num: int, lower_bound: float, upper_bound: float) -> bool:
    assert lower_bound <= upper_bound, "Internal error: wrong interval bounds"
    if f_num == 0:
        return lower_bound > 0.0
    elif f_num == 1:
        return True
    else:
        raise IndexError("Internal error: wrong function number")


def main():
    # interaction
    print("Functions:")
    for i in range(len(functions)):
        print(f"{i + 1}) {functions[i][1]}")
    f_num = read_int("Enter function number", min_val=1, max_val=len(functions)) - 1
    lower_bound = read_float("Enter lower bound of the interval")
    upper_bound = read_float("Enter upper bound of the interval", min_val=lower_bound)
    while not is_valid_interval(f_num, lower_bound, upper_bound):
        print(f"Function has a discontinuity or is not defined on this interval: "
              f"[{lower_bound}, {upper_bound}], please enter correct bounds")
        lower_bound = read_float("Enter lower bound of the interval")
        upper_bound = read_float("Enter upper bound of the interval", min_val=lower_bound)
    control_points_num = read_int("Enter number of control points", min_val=2)
    add_noise = read_string("Add noise?", ["yes", "no"]) == "yes"
    noise_deviation = 0.0
    if add_noise:
        noise_deviation = read_float("Enter noise deviation", min_val=0.0)
    spline_point_x = read_float("Enter the point you are interested in", min_val=lower_bound, max_val=upper_bound)

    # computation
    function, function_str = functions[f_num]
    control_points = generate_points(function, control_points_num, lower_bound, upper_bound, random_space=add_noise,
                                     add_noise=add_noise, noise_deviation=noise_deviation)
    spline_f = evaluate_spline(control_points)
    spline_point_y = spline_f(spline_point_x)

    # plotting
    print(f"Computed value for point {spline_point_x}: {spline_point_y}")
    draw_function(function, lower_bound, upper_bound, "Original function", "orange")
    draw_function(spline_f, lower_bound, upper_bound, "Spline function", "green")
    draw_points(control_points, "Control points", "red")
    draw_point(spline_point_x, spline_point_y, color="blue", label="Computed point")
    plt.title(f"Function: {function_str}")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()
