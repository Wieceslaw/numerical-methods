import math

from integration.methods.rectangle_solver import rectangular_integration, middle_rule, right_rule, left_rule
from lib.validated_read import read_int, read_float


def fun_1(x: float) -> float:
    return 1 / x


def fun_2(x: float) -> float:
    if x == 0:
        return (fun_2(x - 1e-6) + fun_2(x + 1e-6)) / 2
    return math.sin(x) / x


def fun_3(x: float) -> float:
    return x ** 2


def is_valid_interval(f_num: int, lower_bound: float, upper_bound: float) -> bool:
    assert lower_bound <= upper_bound, "Internal error: wrong interval bounds"
    if f_num == 1:
        return lower_bound > 0 or upper_bound < 0
    elif f_num in [2, 3]:
        return True
    else:
        raise AssertionError("Internal error: wrong function number")


functions = [
    (fun_1, "1 / x"),
    (fun_2, "sin(x) / x"),
    (fun_3, "x^2")
]


def main():
    reverse = False
    print("Functions:")
    for i in range(len(functions)):
        print(f"{i + 1}) {functions[i][1]}")
    f_num = read_int("Enter function number", min_val=1, max_val=len(functions))
    lower_bound = read_float("Enter lower bound of integration.md interval")
    upper_bound = read_float("Enter upper bound of integration.md interval")
    if lower_bound > upper_bound:
        reverse = True
        lower_bound, upper_bound = upper_bound, lower_bound
    while not is_valid_interval(f_num, lower_bound, upper_bound):
        print(f"Function has a discontinuity or is not defined on this interval: "
              f"[{lower_bound}, {upper_bound}], please enter correct bounds")
        lower_bound = read_float("Enter lower bound of integration.md interval")
        upper_bound = read_float("Enter upper bound of integration.md interval")
        if lower_bound > upper_bound:
            reverse = True
            lower_bound, upper_bound = upper_bound, lower_bound

    precision = read_float("Enter desirable integration.md precision", min_val=1e-12)

    function = functions[f_num - 1][0]
    middle_rule_result, middle_rule_error = rectangular_integration(function, middle_rule, lower_bound, upper_bound,
                                                                    epsilon=precision, reverse=reverse,
                                                                    runge_coeff=1 / 3)
    right_rule_result, right_rule_error = rectangular_integration(function, right_rule, lower_bound, upper_bound,
                                                                  epsilon=precision, reverse=reverse)
    left_rule_result, left_rule_error = rectangular_integration(function, left_rule, lower_bound, upper_bound,
                                                                epsilon=precision, reverse=reverse)
    print("\nResults:")
    print(f"Middle rule result: {middle_rule_result}, error: {middle_rule_error}")
    print(f"Right rule result: {right_rule_result}, error: {right_rule_error}")
    print(f"Left rule result: {left_rule_result}, error: {left_rule_error}")


if __name__ == '__main__':
    main()
