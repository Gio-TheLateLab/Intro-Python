# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 08:43:57 2021

@author: Usuario
"""

llaves = 0
oro =  50

if(llaves > 0):
    llaves -= 1
    print("Abriendo la puerta")
elif(oro > 100):
    oro -= 100
    print("Abriendo la puerta")
else:
    print("Llamando a los guardias")    
    
print("Fin del programa")
