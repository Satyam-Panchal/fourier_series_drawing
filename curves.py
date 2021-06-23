import numpy as np
import matplotlib.pyplot as plt
from complex_plotter import complex_plotter

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


# complex_list_1 = [complex(187.08867, 95.147952), complex(101.02767, 40.624952),
#                   complex(175.32867000000002, 10.69095200000001), complex(101.02767, 40.624952)]
# complex_list_2 = [complex(101.02767, 40.624952), complex(26.72667, 70.558952), complex(59.86867, 131.496952),
#                   complex(59.86867, 131.496952)]
# complex_list_3 = [complex(59.86867, 131.496952),
#                   complex(104.769947, 213.815962)]
#
# complex_list_4 = [complex(104.769947, 213.815962), complex(104.769947, 213.815962), complex(21.916398, 154.482122),
#                   complex(15.501930000000002, 213.28142200000002)]
# complex_list_5 = [complex(15.501930000000002, 213.28142200000002), complex(9.087460900000002, 272.08072200000004),
#                   complex(199.91789699999998, 312.705692), complex(148.602147, 205.797872)]
# complex_list_6 = [complex(148.602147, 205.797872), complex(97.286405, 98.89006600000002),
#                   complex(171.052797, 149.136732), complex(171.052797, 149.136732)]
# complex_list_7 = [complex(171.052797, 149.136732), complex(171.052797, 149.136732), complex(107.977187, 81.250276),
#                   complex(187.088967, 95.14829399999999)]
#
# complex_arrays = [cubic_bezier_curve(complex_list_1), cubic_bezier_curve(complex_list_2),
#                        line(complex_list_3), cubic_bezier_curve(complex_list_4),
#                        cubic_bezier_curve(complex_list_5),
#                        cubic_bezier_curve(complex_list_6), cubic_bezier_curve(complex_list_7)]


complex_list_1 = [complex(89.202381, 92.982141), complex(89.202381, 92.982141), complex(50.270833, 94.116071),
                  complex(41.955357, 72.193451)]
complex_list_2 = [complex(41.955357, 72.193451), complex(33.640357, 50.270450999999994),
                  complex(6.803356999999998, 149.678451), complex(6.803356999999998, 149.678451)]
complex_list_3 = [complex(6.803356999999998, 149.678451), complex(6.803356999999998, 149.678451),
                  complex(42.3331186, 111.12488099999999), complex(41.5771666, 125.48797099999999)]
complex_list_4 = [complex(41.5771666, 125.48797099999999), complex(40.821212599999996, 139.851071),
                  complex(41.1991906, 140.60702099999997), complex(41.1991906, 140.60702099999997)]
complex_list_5 = [complex(41.1991906, 140.60702099999997), complex(41.1991906, 140.60702099999997),
                  complex(83.91049960000001, 150.812381), complex(92.6039516, 176.13678099999998)]
complex_list_6 = [complex(92.6039516, 176.13678099999998), complex(101.2974056, 201.46119099999999),
                  complex(101.2974056, 201.839161), complex(101.2974056, 201.839161)]
complex_list_7 = [complex(101.2974056, 201.839161), complex(101.2974056, 201.839161), complex(111.5027556, 153.458211),
                  complex(138.3390656, 148.54452099999997)]
complex_list_8 = [complex(138.3390656, 148.54452099999997), complex(165.1753756, 143.63083099999997),
                  complex(165.1753756, 143.63083099999997), complex(165.1753756, 143.63083099999997)]
complex_list_9 = [complex(165.1753756, 143.63083099999997), complex(165.1753756, 143.63083099999997),
                  complex(165.93133559999998, 125.86595099999997), complex(170.84502559999999, 124.35405099999997)]
complex_list_10 = [complex(170.84502559999999, 124.35405099999997), complex(175.7587156, 122.84214099999997),
                   complex(194.65752559999999, 153.45821099999998), complex(194.65752559999999, 153.45821099999998)]
complex_list_11 = [complex(194.65752559999999, 153.45821099999998), complex(194.65752559999999, 153.45821099999998),
                   complex(188.23192559999998, 56.318331999999984), complex(175.7587156, 70.30345299999998)]
complex_list_12 = [complex(175.7587156, 70.30345299999998), complex(163.2854956, 84.28857099999998),
                   complex(147.7884756, 94.87190399999997), complex(131.5354956, 94.49392799999998)]
complex_list_13 = [complex(131.5354956, 94.49392799999998), complex(115.28252559999999, 94.11595199999998),
                   complex(115.28252559999999, 93.35999799999998), complex(115.28252559999999, 93.35999799999998)]
complex_list_14 = [complex(115.28252559999999, 93.35999799999998), complex(115.28252559999999, 93.35999799999998),
                   complex(111.12478559999998, 79.75285599999998), complex(114.52656559999998, 77.48499799999998)]
complex_list_15 = [complex(114.52656559999998, 77.48499799999998), complex(117.92835559999999, 75.21714099999997),
                   complex(116.41645559999998, 75.21714099999997), complex(116.41645559999998, 75.21714099999997)]
complex_list_16 = [complex(116.41645559999998, 75.21714099999997), complex(116.41645559999998, 75.21714099999997),
                   complex(111.50275559999997, 73.32726199999998), complex(109.61287559999998, 77.48499799999998)]
complex_list_17 = [complex(109.61287559999998, 77.48499799999998), complex(107.72299559999998, 81.64273699999998),
                   complex(108.10097559999998, 81.64273699999998), complex(108.10097559999998, 81.64273699999998)]
complex_list_18 = [complex(108.10097559999998, 81.64273699999998),
                   complex(100.54145559999998, 81.64273699999998)]
complex_list_19 = [complex(100.54145559999998, 81.64273699999998),
                   complex(100.54145559999998, 81.64273699999998)]
complex_list_20 = [complex(100.54145559999998, 81.64273699999998), complex(100.54145559999998, 81.64273699999998),
                   complex(102.43133559999998, 77.48499799999998), complex(98.65156959999997, 75.59511899999998)]
complex_list_21 = [complex(98.65156959999997, 75.59511899999998), complex(94.87180859999998, 73.70523799999998),
                   complex(94.87180859999998, 73.70523799999998), complex(94.87180859999998, 73.70523799999998)]
complex_list_22 = [complex(94.87180859999998, 73.70523799999998), complex(94.87180859999998, 73.70523799999998),
                   complex(98.27359359999998, 90.71416499999998), complex(89.20216659999998, 92.98202199999997)]

complex_arrays = [C(complex_list_1), C(complex_list_2), C(complex_list_3), C(complex_list_4), C(complex_list_5),
                  C(complex_list_6), C(complex_list_7), C(complex_list_8), C(complex_list_9), C(complex_list_10),
                  C(complex_list_11), C(complex_list_12), C(complex_list_13), C(complex_list_14), C(complex_list_15),
                  C(complex_list_16), C(complex_list_17), L(complex_list_18), L(complex_list_19), C(complex_list_20),
                  C(complex_list_21), C(complex_list_22)]

complex_coordinates = []

for lists in complex_arrays:
    for element in lists:
        complex_coordinates.append(element)

# complex_plotter(complex_coordinates)
