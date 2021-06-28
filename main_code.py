import numpy as np
from math import pi, sin, cos
import matplotlib.pyplot as plt


def complex_plotter(complex_list):
    x = []
    y = []

    for ith_complex_number in range(len(complex_list)):
        x.append(complex_list[ith_complex_number].real)
        y.append(complex_list[ith_complex_number].imag)

    plt.plot(x, y)
    plt.title('complex plane')
    plt.xlabel('real numbers')
    plt.ylabel('imaginary numbers')
    plt.grid()
    plt.show()


# path string for music note, others are available in path string file

path_string = "M10.205357,107.72321H73.70535699999999C73.70535699999999,107.72321,74.27232199999999,120.38542,82.77678399999999,123.22023999999999C91.28124899999999,126.05505999999998,96.38392599999999,124.92112999999999,96.38392599999999,124.92112999999999C96.38392599999999,124.92112999999999,98.462797,126.24404999999999,99.407738,116.79463999999999C100.35267999999999,107.34523999999999,100.54167,109.42410999999998,100.91964,112.06993999999999C101.29762,114.71576999999999,102.05357000000001,118.87350999999998,102.05357000000001,118.87350999999998C102.05357000000001,118.87350999999998,104.51042000000001,116.60564999999998,107.15625000000001,117.73957999999998C109.80208000000002,118.87350999999998,109.99107000000001,119.25148999999998,109.99107000000001,119.25148999999998L110.18006000000001,110.55802999999997C110.18006000000001,110.55802999999997,111.50297,110.36904999999997,111.88095000000001,114.52677999999997C112.25893,118.68451999999998,112.63690000000001,122.27529999999997,112.82589000000002,123.40921999999998C113.01488000000002,124.54314999999998,117.17262000000001,126.62201999999998,127.75595000000001,123.59820999999998C138.33928,120.57439999999998,136.82738,108.29017999999998,136.82738,108.29017999999998L200.89434,107.72320999999998C200.89434,107.72320999999998,179.91666,116.22767999999998,174.24702,128.13393C168.57738,140.04018,172.35714,150.8125,172.35714,150.8125C172.35714,150.8125,154.78125,147.22172,137.39434,151.00149C120.00744,154.78125,111.88095,167.44344999999998,111.88095,167.44344999999998C111.88095,167.44344999999998,106.77826999999999,175.19196,106.02232,178.78274C105.26637,182.37350999999998,105.83332999999999,182.37350999999998,105.83332999999999,182.37350999999998C105.83332999999999,182.37350999999998,104.88838999999999,172.35714,93.17113099999999,159.88393C81.45386699999999,147.41071,41.010415999999985,151.37946,40.065474999999985,150.8125C39.120533999999985,150.24553,44.60118999999999,141.55208,36.852676999999986,127.56696C29.104165999999985,113.58184,10.205356999999985,107.72321,10.205356999999985,107.72321Z"

tc = lambda t: list((complex(t[x], t[x + 1]) for x in range(0, len(t), 2)))


def getNum(string, index):
    # returns tuple
    x = ''
    while True:
        if string[index].isalpha(): break
        x += string[index]
        index += 1
    return eval(x), index


def goodData(data):
    FINAL = []
    dat = []
    x = 1
    pp1, x = getNum(data, x)
    pp2 = 0
    while True:
        if data[x] == "C":
            x += 1
            ls = getNum(data, x)
            x = ls[1]
            dat = pp1 + ls[0]
            pp2 = dat[-4:-2]
            pp1 = dat[-2:]
            FINAL.append(tc(dat))
        elif data[x] == 'S':
            x += 1
            ls = getNum(data, x)
            x = ls[1]
            dat = pp1 + (2 * pp1[0] - pp2[0], 2 * pp1[1] - pp2[1]) + ls[0]
            pp2 = dat[-4:-2]
            pp1 = dat[-2:]
            FINAL.append(tc(dat))
        elif data[x] == 'H':
            x += 1
            ls = getNum(data, x)
            x = ls[1]
            dat = pp1 + (ls[0], pp1[1])
            pp1 = dat[-2:]
            FINAL.append(tc(dat))
        elif data[x] == 'V':
            x += 1
            ls = getNum(data, x)
            x = ls[1]
            dat = pp1 + (pp1[0], ls[0])
            pp1 = dat[-2:]
            FINAL.append(tc(dat))
        elif data[x] == 'L':
            x += 1
            ls = getNum(data, x)
            x = ls[1]
            dat = pp1 + ls[0]
            pp1 = dat[-2:]
            FINAL.append(tc(dat))
        elif data[x] == 'Z':
            break
    return FINAL


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

# for testing out the function
# complex_plotter(new_list)


def nth_fourier_coefficient(n):
    def f(t):
        i = int(t * len(new_list))  # list of complex numbers assigned to f(t)
        return new_list[i]

    dt = 0.001  # numerical integration
    t = 0
    integral = 0
    while t < 1:
        integral += complex(cos(-2 * pi * n * t), sin(-2 * pi * n * t)) * f(t) * dt
        t += dt

    return integral


coeff = []
string = []
js_string = []
no_of_coeff = 200

for n in range(0, no_of_coeff+1):

    if n == 0 :
        coeff.append(nth_fourier_coefficient(n))
        string_element = str(nth_fourier_coefficient(n))
        string.append(string_element)
    else: 
        coeff.append(nth_fourier_coefficient(int(sin(pi/2) * n)))
        coeff.append(nth_fourier_coefficient(int(sin((3*pi)/2) * n)))
        string_element_pos = str(nth_fourier_coefficient(int(sin(pi/2) * n)))
        string_element_neg = str(nth_fourier_coefficient(int(sin((3*pi)/2) * n)))
        string.append(string_element_pos)
        string.append(string_element_neg)

for letter in string:
    new_letter = ""
    for char in letter:
        if char == "j":
            char = "i"
        if char == "(" or char == ")":
            char = ""

        new_letter += char

    js_string.append(new_letter)

print(js_string)
