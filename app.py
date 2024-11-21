def recorrer_lista(lista1, dato): 
    for i in lista1: 
        lista1.append(dato)
    return lista1

resultado_lista = recorrer_lista([], "juan pablo")

print(resultado_lista)