# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 07:54:09 2021

@author: Gio
"""

"""
https://docs.google.com/document/d/1gYJ9-Wk_G2pMffkFoaMqYXJTQMhYiGLQa9fcRbM3fJo/edit?usp=sharing
Salario mensual
Tipo de contrato: 1. dependiente | 2. independiente
Si y sólo si el tipo de contrato es independiente se pide que se ingrese un número de 1 a 5 equivalente a la clase del riesgo.
"""

SMMLV = 908526
riesgos = [0.522,1.044,2.436,4.350,6.960]

salario = int(input("Por favor ingrese su salario: "))
print("Por favor ingrese su tipo de contrato")
tipoContrato = int(input("1: dependiente | 2: indendiente: "))
while(tipoContrato != 1 and tipoContrato != 2):
    tipoContrato = int(input("1: dependiente | 2: indendiente: "))


# Revisión de la base de cotización
baseCotizacion = 0.4*salario
if(baseCotizacion < SMMLV):
    baseCotizacion = SMMLV


if(tipoContrato == 1):
    print("Dependiente")
    pension = 0.04 * baseCotizacion
    eps = 0.04 * baseCotizacion
    arl = 0
    bonificaciones = salario
    
        
if(tipoContrato == 2):
    print("Independiente")
    pension = 0.16 * baseCotizacion
    eps = 0.125 * baseCotizacion
    tipoRiesgo = int(input("Ingrese su tipo de riesgo (1-5): "))
    while(tipoRiesgo < 1 or tipoRiesgo > 5):
        tipoRiesgo = int(input("Ingrese su tipo de riesgo (1-5): "))
    
    arl = riesgos[tipoRiesgo-1] * (baseCotizacion / 100)
    bonificaciones = 0


salarioReal = salario - (pension + eps + arl)
salarioAnual = salarioReal*12 + bonificaciones

print("Salario real", salarioReal)
print("Salario anual", salarioAnual)

    

    
