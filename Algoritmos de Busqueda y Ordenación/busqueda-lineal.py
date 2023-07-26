import random, time

def busqueda_lineal (lista,objetivo):
    match = False
    
    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
    return match

if __name__ == '__main__':
    tamaño_lista = int(input('Ingrese el tamaño de la lista a generar: '))
    lista = [i+1 for i in range(tamaño_lista)]
    print(lista)
    
    objetivo = int(input('Ingrese el numero a buscar: '))
    comienzo = time.time()
    
    encontrado = busqueda_lineal(lista,objetivo)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    
    final = time.time()
    
    print(f'Tiempo de ejecucion: {final-comienzo}')