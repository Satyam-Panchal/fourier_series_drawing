from complex_plotter import complex_plotter
from fourier_coefficient import *

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
