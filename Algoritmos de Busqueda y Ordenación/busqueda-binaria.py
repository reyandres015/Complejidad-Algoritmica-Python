import random, time

def busqueda_binaria(lista, comienzo, final, objetivo):
    while(True):
        if comienzo >= final:
            return False
        medio = int((comienzo + final)/2)
        if lista[medio] == objetivo:
            return medio
        else:
            if lista[medio] > objetivo:
                final = medio
            else:
                comienzo = medio


if __name__ == '__main__':
    tamaño_lista = int(input('Ingrese el tamaño de la lista a generar: '))
    lista = sorted([random.randint(0, 100) for _ in range(tamaño_lista)])
    print(lista)
    
    objetivo = int(input('Ingrese el numero a buscar: '))
    
    comienzo = time.time()
    encontrado = busqueda_binaria(lista, 0, len(lista),objetivo)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista en la posicion {encontrado}')
    final = time.time()
    
    print(f'Tiempo de ejecucion: {final-comienzo}')