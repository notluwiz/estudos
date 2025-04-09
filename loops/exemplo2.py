# Solicitar nomes e idades de 5 pessoas

while True:                 # laço de repetiçao infinito
    nome = input('Digite seu nome (Digite sair para finalizar): ')
    if nome == "SAIR":
        break               # interrompe o laço de repetiçao
    idade = int(input('Digite a sua idade:'))

print("Fim")