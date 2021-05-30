import math


def f11(x, y, z):
    return math.exp(pow(z, 6) - pow(x, 8) + 23) - 74 * z - 47 - (22 * z + 77 * pow(y, 6)) / (
            math.log(pow(z, 5) + pow(z, 4) - 18) + abs(z)) - (58 * pow(z, 6) - x / 60 + 46)


def f12(x):
   a = {
        x < 2: math.exp(pow(x,6) - pow(x, 8) +23) - 74*pow(x, 3) - 47,
        2 <= x < 34: 22*pow((23*pow(x, 4) + 98*x),6) + pow(x, 8)/61,
        34 <= x < 72: math.tan(pow(x, 7)/61 + pow(x, 5)/84) + pow(x, 6)/35,
        72 <= x < 139: 57*pow(x, 8) - 73*pow(x, 3) - 46,
        x >= 139: pow((pow(x,6) + pow(x,7)/99), 8)+42*x
    }[True]
   return a


if __name__ == '__main__':
    print(f11(22,36,33))
    print(f12(24))

