import matplotlib.pyplot as plt
import numpy as np

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

