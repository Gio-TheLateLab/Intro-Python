# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 08:46:10 2021
Ejemplo de ordenamiento de datos
@author: Usuario
"""

nombres = [ "Nezuko", "Tanjiro", "Zenitsu", "Inosuke", "Genya", "Kanao", "Tomioka" ];
estatura = [ 153, 165, 164.5, 164, 180, 156, 176 ];

"""
CSharp
for(int i=0; i<nombres.Length; i+= 2){
}

Python
for i in range(0, len(nombres), 2):
"""

# Ordenamiento de datos
for j in range(0, len(nombres)):
    for i in range(0, len(nombres)-1):
        if(estatura[i] > estatura[i+1]):
            tmp = estatura[i]
            estatura[i] = estatura[i+1]
            estatura[i+1] = tmp
            
            tmp = nombres[i]
            nombres[i] = nombres[i+1]
            nombres[i+1] = tmp
        
print(estatura)
print(nombres)
        
    
    
