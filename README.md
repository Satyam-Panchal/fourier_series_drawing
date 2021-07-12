# fourier_series_drawing

It is easier to understand if you just see what this code does first before reading all the things below , here you go : https://youtu.be/vMIwgcIMirU

If you just want to make some drawings and want to know how can you do just that, go here : https://youtu.be/0zXPP7o7_tU

This Program Draws any closed curve using famous method of fourier epicycle drawings.
This program uses the svgs(scalable vector graphics), it is kind of like a photo file format like png or jpeg.For any drawing you want to make you must have its svg file with you.
This code is not yet fully automated hence here are some instructions on how can you make your own drawings with it.
I have created TWO copies of the same code, you should be using the main_code.py file , this file takes in an ABSOLUTE svg file's path and gives you the list of fourier coefficients. Remember the path should be one continuous string, i.e. the drawing must be in a form of (any) closed loop. 
If you do not have the absolute path use the following website to convert the relative path to absolute : https://jsbin.com/mudusiseta/1/edit?html,js,output
OR If you do not want to go through all this process i have added some absolute svg paths for some svgs i made in the path_strings.py file, you may copy the path of any svg present there, i will update it later on with more svg paths.
Once you feed in the absolute path of svg the main_code.py will provide you with a list of strings, these strings are actually complex fourier coefficients for your drawing, but they are printed in form of string so i can feed them easily to java script code.
Now this is the embarrassing part as of now, but you will have to copy that string of fourier coefficients, and paste it in the js code , in the file animating_the_drawing.js, once you run it, your drawing should pop up on the browser.

Again , if you dont wanna go through the hassle, you can just run the animating_the_drawing.js code, it is using the "Batman logo" drawing as an example. and as i said to make it draw something else, you will have to paste the coefficient list for the particular drawing you want, that list you will get from python main_code.py

for the python code in the folder, here is what each file does:
curves.py --> calculates the complex points of sections of drawings , the bezier curves, to form the function(the same function we are approximating, that is the drawing) that traces the given curve when plotted on a complex point
path_strings.py --> contains example path strings of svgs for different drawings
fourier_coefficients --> calculates the complex fourier coefficients given the function f(t).
converting_path_to_array --> converts the ABSOLUTE svg path to a 2D array of complex numbers , to feed each list to a bezier curve/line plotter to make up the function f(t)
complex_plotter--> just a peice of code for checking the whether the points calculated by the code are correctly plotting the desired shape on the complex plane, can also be used to check correctness of fourier coefficients using with testing_coefficients.py
testing_coefficient.py --> can be used to test the fourier coefficients calculated by the program with the help of complex_plotter.py
bring_everything_together.py --> to calculate the final list of fourier coefficients in the form suitable for feeding into java script code

I will be updating the code and this read me file at regular intervals.
