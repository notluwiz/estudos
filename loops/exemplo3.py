# Solicitar nomes e idades de 10 pessoas
# Contar quantas pessoas são menores de idade (idade < 18)

contaMenores = 0            # contadora

while True:                 # laço de repetiçao infinito
    nome = input('Digite seu nome (Digite sair para finalizar): ')
    if nome == 'SAIR':
        break               # interrompe o laço de repetiçao
    idade = int(input('Digite a sua idade:'))
    if idade < 18:
        contaMenores += 1

print(f'Quantidade de pessoas menores de idade {contaMenores}')
print("Fim")