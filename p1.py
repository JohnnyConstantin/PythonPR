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


# def f22(x):
#     ed = x >> 27
#     c = (x - (ed << 27)) >> 24
#     b = (x - (ed << 27) - (c << 24)) >> 14
#     a = (x - (ed << 27) - (c << 24) - (b << 14))
#     return int((c << 29) + (a << 15) + (ed << 10) + b)

def f22(x):
    G = x >> 30
    F = (x - (G << 30)) >> 25
    E = (x - (G << 30) - (F << 25)) >> 19
    D = (x - (G << 30) - (F << 25) - (E << 19)) >> 18
    C = (x - (G << 30) - (F << 25) - (E << 19) - (D << 18)) >> 10
    B = (x - (G << 30) - (F << 25) - (E << 19) - (D << 18) - (C << 10)) >> 4
    A = (x - (G << 30) - (F << 25) - (E << 19) - (D << 18) - (C << 10) - (B << 4))
    return int((D << 31) + (B << 25) + (C << 17) + (G << 15) + (A << 11) + (E << 5) + F)


class C32():

    S0 = 'A'

    def add(self):
        if self.S0 == 'A':
            self.S0 = 'B'
            return 0
        elif self.S0 == 'F':
            self.S0 = 'B'
            return 8
        elif self.S0 == 'G':
            self.S0 = 'B'
            return 10
        elif self.S0 == 'D':
            self.S0 = 'E'
            return 4
        elif self.S0 == 'C':
            self.S0 = 'C'
            return 3
        else:
            return None

    def warp(self):
        if self.S0 == 'B':
            self.S0 = 'C'
            return 1
        elif self.S0 == 'F':
            self.S0 = 'G'
            return 7
        elif self.S0 == 'G':
            self.S0 = 'C'
            return 11
        elif self.S0 == 'C':
            self.S0 = 'D'
            return 2
        elif self.S0 == 'E':
            self.S0 = 'F'
            return 6
        else:
            return None

    def turn(self):
        if self.S0 == 'D':
            self.S0 = 'D'
            return 5
        elif self.S0 == 'G':
            self.S0 = 'H'
            return 9
        else:
            return None

if __name__ == '__main__':
    o = C32()
    print(o.add())
    print(o.warp())
    print(o.add())
    print(o.warp())
    print(o.warp())
    print(o.turn())
    print(o.add())
    print(o.warp())
    print(o.add())
    print(o.warp())
    print(o.add())
    print(o.add())
    print(o.warp())
    print(o.add())
    print(o.warp())
    print(o.warp())
    print(o.add())