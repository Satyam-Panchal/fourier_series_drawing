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
path_string = "M83.721725,175.19196C83.721725,175.19196,85.233631,175.56994,92.98214100000001,169.33333C100.73065000000001,163.09671999999998,100.91964000000002,161.77381,106.40030000000002,160.82887C111.88095000000001,159.88393,113.58184000000001,158.75,122.27530000000002,159.88393C130.96875000000003,161.01785999999998,138.52827000000002,164.04165999999998,140.41815000000003,167.82143C142.30803000000003,171.60119,146.65476000000004,179.34969999999998,138.90625000000003,185.20833C131.15774000000002,191.06696,123.40922000000003,193.33481999999998,118.68452000000002,193.7128C113.95982000000002,194.09077,100.73065000000003,193.90177999999997,95.24999900000002,193.14583C89.76899900000002,192.38983,75.40599900000001,190.49983,72.38199900000002,176.70382999999998C69.35899900000003,162.90783,73.70499900000002,151.75782999999998,80.50899900000002,144.57583C87.31199900000001,137.39482999999998,94.87199900000002,128.51183,97.89599900000002,126.99983C100.91980700000002,125.48792,114.90492700000001,113.01471000000001,119.06266700000002,108.66798C123.22040700000002,104.32126,136.44956700000003,89.958162,140.41831700000003,77.484947C144.38706700000003,65.011735,145.89897700000003,59.90905500000001,142.87516700000003,49.89268700000001C139.85135700000004,39.87631900000001,128.89004700000004,27.78108000000001,120.00760700000004,27.21411500000001C111.12516700000003,26.64715200000001,98.08498800000004,30.04893700000001,94.49421400000003,37.04149600000001C90.90344000000003,44.03405500000001,87.12367700000003,55.94030500000001,89.76951000000003,67.84655500000001C92.41534300000002,79.75280500000001,98.27397500000002,118.49536,98.27397500000002,118.49536L106.40046700000002,157.99388L111.69212700000003,192.76769L114.14897700000003,209.39864C114.14897700000003,209.39864,116.03885700000004,230.37632,114.90492700000003,236.23495C113.77099700000002,242.09358,109.61325700000003,246.06233,106.40046700000003,246.06233C103.18766700000003,246.06233,99.59689200000004,244.9284,99.59689200000004,244.9284C99.59689200000004,244.9284,108.66831700000004,241.52661,105.83349700000004,233.58911C102.99867700000004,225.65161,98.27397500000004,224.3287,94.11623800000004,224.51768C89.95849900000003,224.70667,86.55671400000004,225.65161,83.15492700000004,226.78554000000003C79.75314200000004,227.91947000000002,74.83945100000004,234.53405000000004,74.83945100000004,237.36888000000002C74.83945100000004,240.20370000000003,72.76058300000004,247.95221,84.47784300000004,253.24388000000002C96.19510700000004,258.53554,106.40046700000003,259.66947000000005,114.33796700000003,253.62185000000002C122.27546700000003,247.57423000000003,125.86623700000004,242.28257000000002,125.11028700000003,228.67542000000003C124.35433700000003,215.06828000000004,122.08647700000003,207.31977000000003,122.08647700000003,207.31977000000003L116.79480700000003,170.65608000000003L104.51058700000003,97.32869700000003C104.51058700000003,97.32869700000003,97.51802300000003,65.20072200000004,100.91980700000003,54.428402000000034C104.32159700000004,43.656079000000034,108.66831700000003,37.608461000000034,113.95998700000004,35.90756900000004C119.25165700000004,34.206674000000035,134.37069700000004,39.12036400000004,130.40194700000004,58.77512800000004C126.43319700000004,78.42988800000003,116.79480700000003,88.63524600000004,111.12516700000003,93.35994700000003C105.45552700000003,98.08465100000004,91.47040500000003,106.02215000000004,85.98974900000003,111.12483000000003C80.50909300000004,116.22751000000004,70.30373900000004,120.95221000000004,61.04332200000003,136.82721000000004C51.78290600000003,152.70221000000004,43.656416000000036,169.52215000000004,58.77546500000003,187.28703000000004C73.89451000000003,205.05191000000005,99.40790500000003,208.26471000000004,109.61325700000003,208.26471000000004C119.81861700000003,208.26471000000004,153.26950700000003,200.32721000000004,158.37218700000003,179.16054000000003C163.47486700000002,157.99388000000002,136.44956700000003,148.35548000000003,136.44956700000003,148.35548000000003C136.44956700000003,148.35548000000003,125.29927700000003,143.81977000000003,114.33796700000003,146.27661000000003C103.37665700000004,148.73346000000004,94.11623800000004,151.75727000000003,88.25760700000004,161.20667000000003C82.39897500000004,170.65608000000003,81.83201000000004,171.60102000000003,82.77695100000004,173.49090000000004C83.72189200000004,175.38078000000004,83.72189200000004,175.19179000000003,83.72189200000004,175.19179000000003Z"

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

for n in range(-200, 201):
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

print(js_string)
