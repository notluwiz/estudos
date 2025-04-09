# importaçao de um modulo
import funcoes

quantidade = int(input('Informe o tamanho da lista: '))
listasNumeros = funcoes.criar_lista_aleatoria(quantidade)
print(listasNumeros)

lista2 = funcoes.criar_lista(5)
print(lista2)

numero1 = float(input('Digite um numero: '))
numero2 = float(input('Digite outro numero: '))
resultado = funcoes.somar(numero1, numero2)
print(resultado)

resultado = funcoes.somar(10, 20)
print(resultado)