def imprimir_Arreglo(arreglo):
    i = 0
    while i < len(arreglo)-1:
        print(f'[{arreglo[i]}]', end="")
        i += 1
    print(f'[{arreglo[len(arreglo)-1]}]')

def algoritmo_Burbuja(arreglo):
    i = 0
    while i < len(arreglo)-1:
        j = 0
        while j < len(arreglo)-1-i:
            if arreglo[j] > arreglo[j+1]:
                aux = arreglo[j]
                arreglo[j] = arreglo[j+1]
                arreglo[j+1] = aux
            j += 1
        i += 1

listaSueldos = [20.8, 150.5, 170.5, 180.8, 190, 30, 75.6, 200]
imprimir_Arreglo(listaSueldos)
algoritmo_Burbuja(listaSueldos)
print("")
imprimir_Arreglo(listaSueldos)
