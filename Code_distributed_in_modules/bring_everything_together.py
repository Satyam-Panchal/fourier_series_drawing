from complex_plotter import complex_plotter
from fourier_coefficient import *

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