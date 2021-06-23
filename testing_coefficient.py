from fourier_coefficient import coeff
from complex_plotter import complex_plotter
from math import pi, sin, cos


def f(t):
    return sum([
        coeff[k+50] * complex(cos(2 * pi * k * t), sin(2 * pi * k * t))
        for k in range(-50, 51)
    ])


points = []

t = 0
while t <= 1:
    points.append(f(t))
    t += 0.0001

complex_plotter(points)