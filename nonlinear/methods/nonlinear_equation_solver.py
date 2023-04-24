from typing import Callable


def bisection_method(f: Callable[[float], float],
                     l: float, r: float, e: float,
                     max_i: int = 1000) -> float:
    i = 0
    while abs(r - l) > e and i < max_i:
        i += 1
        m = (r + l) / 2
        fm = f(m)
        fr = f(r)
        if fm == 0:
            return m
        elif fm * fr > 0:
            r = m
        else:
            l = m
    return (r + l) / 2


def secant_method(f: Callable[[float], float],
                  l: float, r: float, e: float,
                  max_i: int = 1000) -> float:
    i = 0
    x = l
    while abs(r - l) > e and i < max_i:
        i += 1
        x = l - f(l) / (f(l) - f(r)) * (l - r)
        fm = f(x)
        fr = f(r)
        if fm == 0:
            return x
        if fm * fr > 0:
            r = x
        else:
            l = x
    return x
