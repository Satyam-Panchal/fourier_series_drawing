from bring_everything_together import coeff
from complex_plotter import complex_plotter
from math import pi, sin, cos

list = [
    complex(66.75, -53.07),
    complex(-135.66, -45.57),
    complex(10.72, 16.52),
    complex(-12.64, 20.90),
    complex(-44.85, -23.71)
]


def f(t):
    return sum([
        coeff[200 + k] * complex(cos(2 * pi * k * t), sin(2 * pi * k * t))
        for k in range(-200, 201)
    ])


points = []

t = 0
while t <= 1:
    points.append(f(t))
    t += 0.0001

complex_plotter(points)