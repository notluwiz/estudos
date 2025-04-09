# Solicitar 10 numeros e verificar se sao pares ou impares

contador = 1                # variavel contadora
while contador <= 10:

    numero = int(input('Digite um numero'))
    if numero % 2 == 0:
        print('Par')
    else:
        print('Impar')

    contador += 1       # contador = contador + 1

print('Fim')