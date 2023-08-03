import random, time

def busqueda_binaria(lista, comienzo, final, objetivo, contador):
    if comienzo > final or comienzo >= len(lista) or final > len(lista):
        print(f'Iteraciones (no encontrado): {contador}')
        return None
    else: 
        print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
        

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        print(f'Iteraciones: {contador}')
        return medio
    elif lista[medio] < objetivo:
        contador+=1
        return busqueda_binaria(lista, medio + 1, final, objetivo, contador)
    else:
        contador+=1
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo, contador)


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano es la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = sorted([i for i in range(tamano_de_lista)])
    
    comienzo = time.time()
    index = busqueda_binaria(lista, 0, len(lista), objetivo, 1)
    final = time.time()
    
    print(f'El elemento {objetivo} {f"esta en la lista en la posición {int(index)}" if index != None else "no esta"}')

    print(f'Tiempo de ejecucion: {final-comienzo}')
