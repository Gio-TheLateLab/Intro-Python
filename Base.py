import math

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 07:12:29 2021
CSharp comparison found in slide number 6
https://docs.google.com/presentation/d/e/2PACX-1vQb9uu3OhtSsPhxYmF44YWSBLwkGZ9NAGDEXVT-uWn79gPt3LM6lp7aGJOiBpfY5hz5VjNdxKHsh2WY/pub?start=false&loop=false&delayms=3000
@author: Gio-TheLateLab
"""


# Input. we use the input function to the read data and parse it to a float
anguloRad = float(input('Ingrese el ángulo en radianes: '))

# Process
anguloGrad = anguloRad * (180.0/math.pi)

# Output. We use "," instead of "+"
print("Ángulo = ",anguloGrad)


