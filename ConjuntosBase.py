# Actividad completa: https://docs.google.com/document/d/1eJMLLf129gaviK1CMYpsVgZ_PVaQBjW0pHD3tYP-sLE/edit?usp=sharing

# Datos del conjunto A
A = [0,3,6,9,12,15,18,6,12]

# Datos del conjunto B
B = [0,2,4,6,8,10,12,14,16,18,2,6]

# Se imprimen los conjuntos
print("\nConjunto A:", A)
print("\nConjunto B:", B)
    
# Se almacenan ambos conjuntos (arreglos) a una misma lista llamada unionTMP
unionTMP = []
for i in range(0, len(A)):
    unionTMP.append(A[i])
for i in range(0, len(B)):
    unionTMP.append(B[i])

print("\nAmbos conjuntos:",unionTMP)

# Ahora debemos elimitar los repetidos

# Empezamos un arreglo llamado unión que inicia con el primer valor de la lista
# Como es el primer valor no será un dato repetido
union = [unionTMP[0]]
for i in range(0, len(unionTMP)):

    # Recorremos cada datos de la lista compartida (unionTMP)
    repetido = False # La premisa es que el dato es nuevo
    for j in range(0, len(union)): # Se recorre la lista donde almacenaremos la unión
        if(unionTMP[i] == union[j]): # Si el dato ya se encuentra en la unión
            repetido = True # significa que es un dato repetido

    if(repetido == False): # Si al final de recorrer cada dato de la unión la variable repetido sigue en falso
        union.append(unionTMP[i]) # Almacenamos el dato a la unión

print("\nUnión:",union)

