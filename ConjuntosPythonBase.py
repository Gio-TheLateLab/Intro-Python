# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 08:28:15 2021

@author: Gio
"""
# Actividad completa: https://docs.google.com/document/d/1eJMLLf129gaviK1CMYpsVgZ_PVaQBjW0pHD3tYP-sLE/edit?usp=sharing

# Datos del conjunto A
A = [0,3,6,9,12,15,18,6,12]

# Datos del conjunto B
B = [0,2,4,6,8,10,12,14,16,18,2,6]

unionTMP = A + B
union = []
for i in unionTMP:
    if i not in union:
        union.append(i)

union.sort()
print('Union:',union)

