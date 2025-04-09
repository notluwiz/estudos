# Solicitar os nomes e idades de 10 pessaos

quantidade = int(input('Informe a qunatidade de pessoas: '))

contaMenores = 0

for numero in range(quantidade):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    if idade < 18:
        contaMenores += 1

print(f'Quantidade de menores de idade {contaMenores}')