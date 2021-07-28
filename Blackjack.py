# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 15:48:33 2021

@author: Gio
"""

"""
Descripción:
Crear un juego (consola) en donde el objetivo del jugador es sumar entre todas sus cartas un total de 21. En el El jugador inicia con dos cartas, sin embargo puede pedir cartas adicionales (siempre y cuando no haya sido eliminado). Especificaciones:
El jugador recibe 2 cartas al iniciar (primer turno).
Las cartas son números aleatorios entre 1 y 10
Mientras el jugador lo desee y no esté eliminado, puede solicitar cartas adicionales. Una carta por turno
En cada turno se debe mostrar el valor de la carta o cartas y, el total
Si el jugador es eliminado se muestra un mensaje indicando que no puede continuar. Tampoco se le debe preguntar si desea continuar
Al finalizar el juego se muestra el total
"""

import random

carta1 = random.randint(1,10)
carta2 = random.randint(1,10)

total = carta1 + carta2
print("Carta 1:", carta1, " Carta 2:", carta2, " Total:", total)

respuesta = input("Desea continuar (s/n): ")
while(respuesta == "s"):
    carta = random.randint(1,10)
    total += carta
    print("Carta:", carta, " Total:", total)
    if(total > 21):
        print("Eliminado", )
        break
    
    respuesta = input("Desea continuar (s/n): ")
    
print("Fin del turno, su total es:",total)
        