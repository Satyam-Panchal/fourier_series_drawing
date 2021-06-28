from math import pi, factorial, sin, cos
from curves import new_list


def nth_fourier_coefficient(n):
    def f(t):
        i = int(t * len(new_list))  # list of complex numbers assigned to f(t)
        return new_list[i]

    dt = 0.001                                   # numerical integration
    t = 0
    integral = 0
    while t < 1:
        integral += complex(cos(-2 * pi * n * t), sin(-2 * pi * n * t)) * f(t) * dt
        t += dt

    return integral



