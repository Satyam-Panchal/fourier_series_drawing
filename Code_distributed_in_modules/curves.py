import numpy as np
import matplotlib.pyplot as plt
from complex_plotter import complex_plotter
from Bezier import *
from path_strings import path_string

# Dimensions of drawing paper
height = 297
width = 210


def C(complex_list):
    corrected = []

    for z in complex_list:
        real = z.real
        imag = z.imag

        corrected_real = real - (width / 2)
        corrected_imag = (height / 2) - imag
        corrected.append(complex(corrected_real, corrected_imag))

    p0 = corrected[0]
    p1 = corrected[1]
    p2 = corrected[2]
    p3 = corrected[3]

    t = np.linspace(0, 1, 1000)
    complex_coordinate = np.array(
        ((1 - t) ** 3) * p0 + 3 * t * ((1 - t) ** 2) * p1 + 3 * (t ** 2) * (1 - t) * p2 + (t ** 3) * p3, dtype=complex)

    return complex_coordinate


def Q(complex_list):
    corrected = []

    for z in complex_list:
        real = z.real
        imag = z.imag

        corrected_real = real - (width / 2)
        corrected_imag = (height / 2) - imag
        corrected.append(complex(corrected_real, corrected_imag))

    p0 = corrected[0]
    p1 = corrected[1]
    p2 = corrected[2]

    t = np.linspace(0, 1, 1000)
    complex_coordinate = np.array(((1 - t) ** 2) * p0 + 2 * t * (1 - t) * p1 + (t ** 2) * p2, dtype=complex)

    return complex_coordinate


def L(complex_list):
    corrected = []

    for z in complex_list:
        real = z.real
        imag = z.imag

        corrected_real = real - (width / 2)
        corrected_imag = (height / 2) - imag
        corrected.append(complex(corrected_real, corrected_imag))

    p0 = corrected[0]
    p1 = corrected[1]

    t = np.linspace(0, 1, 1000)
    complex_coordinate = np.array((1 - t) * p0 + t * p1, dtype=complex)

    return complex_coordinate



converted_array = goodData(path_string)



complex_coordinates = []

for list in converted_array:
    if len(list) == 4:
        cubic_bezier_curve_info = C(list)
        for elements in cubic_bezier_curve_info:
            complex_coordinates.append(elements)
    elif len(list) == 2:
        line_info = L(list)
        for elements in line_info:
            complex_coordinates.append(elements)
    else:
        quadratic_bezeir_curve_info = Q(list)
        for elements in quadratic_bezeir_curve_info:
            complex_coordinates.append(elements)


new_list = complex_coordinates


