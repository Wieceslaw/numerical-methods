from lib.validated_read import read_string, read_int, read_float
from methods.nonlinear_equation import bisection_method, secant_method
from methods.nonlinear_system import newton_method


def main():
    system = [
        lambda x: (x[0] - 1) ** 3 - x[0] ** 2 + x[1],
        lambda x: x[0] ** 2 + x[0] ** 5 - x[1]
    ]
    system_str = """
    | (x - 1)^3 - x^2 + y = 0
    | x^2 - y + x^5 = 0
    """
    equations = [
        (lambda x: (x - 1) ** 3 - x ** 2 + 2, "(x - 1)^3 - x^2 + 2 = 0"),
        (lambda x: (x ** 2 - 2) ** 2 - 2, "(x^2 - 2)^2 - 2 = 0"),
    ]

    while True:
        type_ = read_string("Enter 'system' or 'equation' to choose:", ["system", "equation"])
        if type_ == 'equation':
            print("Equations:")
            print("\n".join([f"{i + 1}) " + eq[1].strip() for i, eq in enumerate(equations)]))
            i = read_int("Enter number of equation:", min_val=1, max_val=len(equations)) - 1
            function = equations[i][0]
            a = read_float("Enter left bound:")
            b = read_float("Enter right bound:", min_val=a)
            while function(a) * function(b) >= 0:
                print("Wrong bounds, please specify such 'a' and 'b' so that f(a) * f(b) < 0")
                a = read_float("Enter left bound:")
                b = read_float("Enter right bound:", min_val=a)
            e = read_float("Enter accuracy epsilon:")
            bisection_result = bisection_method(function, a, b, e)
            secant_result = secant_method(function, a, b, e)
            print("Bisection methods result: {0:0.5f}".format(bisection_result))
            print("Secant methods result: {0:0.5f}".format(secant_result))
        else:
            print("System:")
            print(system_str)
            e = read_float("Enter accuracy epsilon:")
            newton_result = newton_method(system, e)
            print("System solution:")
            for i, el in enumerate(newton_result):
                print(f"x{i + 1}) {'{0:0.5f}'.format(el)}")
        print()


if __name__ == '__main__':
    main()
