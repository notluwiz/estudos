# Solicitar os nomes e idades de 10 pessaos
# Armazenar os nomes e idades em listas

listaNomes = []
listaIdades = []
contaMenores = 0

quantidade = int(input('Informe a qunatidade de pessoas: '))


for numero in range(quantidade):

    nome = input('Digite seu nome: ')
    listaNomes.append(nome)

    idade = int(input('Digite sua idade: '))
    listaIdades.append(idade)

    if idade < 18:
        contaMenores += 1

print(f'Quantidade de menores de idade {contaMenores}')
print(listaNomes)
print(listaIdades)

nome = input('Informe um nome para buscara na lista: ')
if nome in listaNomes:
    print(f'O nome {nome} esta cadastrado na lista')
else:
    print(f'O nome {nome} nao esta cadastrado na lista')

print(f'Quantidade de nomes cadastrados: {len(listaNomes)}')
media = sum(listaIdades) / len(listaIdades)
print(f'Media das idades: {media}')