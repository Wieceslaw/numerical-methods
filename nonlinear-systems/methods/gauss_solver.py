import copy


def max_row(m: list[list[float]], col: int):
    max_i = col
    max_val = abs(m[col][col])
    for row in range(col, len(m)):
        if abs(m[row][col]) > max_val:
            max_i = row
    return max_i


def gauss_forward_elimination(m: list[list[float]]):
    n = len(m)
    for i in range(n):
        i_max = max_row(m, i)
        m[i], m[i_max] = m[i_max], m[i]
        for j in range(i + 1, n):
            factor = m[j][i] / m[i][i]
            for k in range(i + 1, n + 1):
                m[j][k] -= factor * m[i][k]
            m[j][i] = 0


def gauss_back_substitution(m: list[list[float]]) -> list[float]:
    n = len(m)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = m[i][n] / m[i][i]
        for j in range(i - 1, -1, -1):
            m[j][n] -= x[i] * m[j][i]
    return x


def gauss_elimination(a: list[list[float]], b: list[float]) -> list[float]:
    m = copy.deepcopy(a)
    for i in range(len(a)):
        m[i].append(b[i])

    gauss_forward_elimination(m)
    return gauss_back_substitution(m)
