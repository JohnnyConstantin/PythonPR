import math

def f11(x, y, z):
    answer = math.exp(pow(z, 6) - pow(x, 8) + 23) - 74*z - 47 - (22*z + 77*pow(y, 6))/(math.log(pow(z, 5) + pow(z, 4) - 18) + abs(z)) - (58*pow(z, 6) - x/60 + 46)
    return answer
