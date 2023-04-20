import math

from approximation.methods.points_generation import generate_points
from lib.plot_gui import show_plot
from lib.validated_read import read_int, read_string, read_float
from methods.spline_interpolation import calc_spline

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
    function, function_str = functions[f_num]

    # computation
    control_points = generate_points(function, control_points_num, lower_bound, upper_bound, random_space=add_noise,
                                     add_noise=add_noise, noise_deviation=noise_deviation)
    spline_f = calc_spline(control_points)
    function_points = generate_points(function, 500, lower_bound, upper_bound)
    spline_function_points = generate_points(spline_f, 500, lower_bound, upper_bound)

    # plotting
    show_plot(control_points, function_points, spline_function_points, function_str)


if __name__ == '__main__':
    main()
