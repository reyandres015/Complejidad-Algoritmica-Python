import random,time

def bubble_sort(lista):
    n = len(lista)
    
    for i in range(n):
        for j in range(0,n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista



if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano es la lista? '))

    lista = [random.randint(0,100) for _ in range(tamano_de_lista)]
    
    comienzo = time.time()
    lista_ordenada =  bubble_sort(lista[:])
    tiempo_ejecucion = time.time() - comienzo
    
    print(lista)
    print(lista_ordenada)

    print(f'Tiempo de ejecucion: {tiempo_ejecucion}')
