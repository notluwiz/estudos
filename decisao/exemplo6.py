nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
faltas = int(input('Informe a quantidade de faltas: '))

media = (nota1 + nota2) / 2

if media >= 6:              # True
    if faltas <= 10:        # True
        print(f'Aprovado com media {media}')
    else:                   # False
        print(f'Reprovado por excesso de faltas = {faltas}.')
else:                       # False
    print(f'Reprovado com a media {media}')