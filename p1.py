import math


def f11(x, y, z):
    return math.exp(pow(z, 6) - pow(x, 8) + 23) - 74 * z - 47 - (22 * z + 77 * pow(y, 6)) / (
            math.log(pow(z, 5) + pow(z, 4) - 18) + abs(z)) - (58 * pow(z, 6) - x / 60 + 46)


def f12(x):
    a = {
        x < 2: math.exp(pow(x, 6) - pow(x, 8) + 23) - 74 * pow(x, 3) - 47,
        2 <= x < 34: 22 * pow((23 * pow(x, 4) + 98 * x), 6) + pow(x, 8) / 61,
        34 <= x < 72: math.tan(pow(x, 7) / 61 + pow(x, 5) / 84) + pow(x, 6) / 35,
        72 <= x < 139: 57 * pow(x, 8) - 73 * pow(x, 3) - 46,
        x >= 139: pow((pow(x, 6) + pow(x, 7) / 99), 8) + 42 * x
    }[True]
    return a


def f13(n, m):
    return sum(math.exp(i) - math.log(i) - 5 for i in range(1, n + 1)) - 29 * sum(
        sum(pow(i, 5) - 48 * pow(j, 4) for j in range(1, m + 1)) for i in range(1, n + 1))


def f14(n):
    if n == 0:
        return 6
    else:
        return 1 / 15 * f14(n - 1) - 1 / 99 * pow(f14(n - 1), 3)

def f21(x):
    if x[4] == 'minid':
        if x[2] == 'cool':
            if x[3] == 1981:
                return 4
            elif x[3] == 1959:
                return 5
        elif x[2] == 'elm':
            return 3
        elif x[2] == 'xslt':
            if x[1] == 'max':
                return 2
            elif x[1] == 'antlr':
                if x[0] == 2018:
                    return 0
                elif x[0] == 2005:
                    return 1
    elif x[4] == 'coq':
        if x[0] == 2018:
            if x[1] == 'antlr':
                if x[2] == 'xslt':
                    return 6
                elif x[2] == 'elm':
                    return 7
                elif x[2] == 'cool':
                    return 8
            elif x[1] == 'max':
                if x[3] == 1981:
                    return 9
                elif x[3] == 1959:
                    return 10
        elif x[0] == 2005:
            return 11
