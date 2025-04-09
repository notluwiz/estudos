import random

def criar_lista(tamanho):
    lista = []
    for i in range(tamanho):
        numero = int(input('Numero: '))
        lista.append(numero)
    return lista            # retorna a lista

def criar_lista_aleatoria(tamanho):
    lista = []
    for i in range(tamanho):
        numero = random.randint(1, 100)
        lista.append(numero)
    return lista

def somar(a, b):
    c = a + b
    return c