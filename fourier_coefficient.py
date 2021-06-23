from math import pi, factorial, sin, cos
from curves import complex_coordinates
import numpy as np


def nth_fourier_coefficient(n):
    def f(t):
        i = int(t * len(complex_coordinates))  # list of complex numbers assigned to f(t)
        return complex_coordinates[i]

    dt = 0.001                                   # numerical integration
    t = 0
    integral = 0
    while t < 1:
        integral += complex(cos(-2 * pi * n * t), sin(-2 * pi * n * t)) * f(t) * dt
        t += dt

    return integral


coeff = []
string = []
js_string = []

for n in range(-50, 51):
    coeff.append(nth_fourier_coefficient(n))
    string_element = str(nth_fourier_coefficient(n))
    string.append(string_element)

for letter in string:
    new_letter = ""
    for char in letter:
        if char == "j":
            char = "i"
        if char == "(" or char == ")":
            char = ""

        new_letter += char

    js_string.append(new_letter)

# print(coeff)
# print(js_string)
# print(len(js_string))
