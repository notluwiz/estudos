# Solicitar nomes e idades de 10 pessoas
# Contar quantas pessoas são menores de idade (idade < 18)
# Calcular a media de idade de todas as pessoas

contaMenores = 0            # contadora
somaIdade = 0
contaPessoas = 0

while True:                 # laço de repetiçao infinito
    nome = input('Digite seu nome (Digite sair para finalizar): ')
    if nome == 'SAIR':
        break               # interrompe o laço de repetiçao
    idade = int(input('Digite a sua idade:'))
    somaIdade += idade      # Soma todas as idades
    contaPessoas += 1
    if idade < 18:
        contaMenores += 1

media = somaIdade / contaPessoas
print(f'Media de idades {media}')
print(f'Quantidade de pessoas menores de idade: {contaMenores}')
print('Fim')