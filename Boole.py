# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 08:51:50 2021

@author: Usuario
"""

creditosMatriculados = int(input("Ingrese la cantidad de créditos matriculados este semestre: "))
creditosCursados = int(input("Ingrese la cantidad de créditos que ha cursado durante la carrera: "))
creditosPerdidos = int(input("Ingrese la cantidad de créditos que ha perdido durante la carrera: "))
promedio = float(input("Ingrese su promedio del semestre anterior: "))
promedioEstudiantes = 3.3

a = creditosMatriculados >= 16
b = creditosPerdidos <= 0.05* creditosCursados
c = promedio >= promedioEstudiantes + 0.2
d = promedio >= 3.8

if( (a and b) and (c or d)):
    print("Puede participar del programa")
else:
    print("No cumple con el perfil")

