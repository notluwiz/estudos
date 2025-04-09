nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
faltas = int(input('Informe a quantidade de faltas: '))

media = (nota1 + nota2) / 2

if media > 6 and faltas <= 10:
    print(f'Aprovado com media {media} e aprovado por faltas {faltas}')
elif media > 6 and faltas > 10:
    print(f'Aprovado por media {media}, e reprovado por falta {faltas}')
elif media < 6 and faltas <= 10:
    print(f'Reprovado por media {media}, e aprovado por falta {faltas}')
else:
    print(f'Reprovado por media {media}, e reprovado por falta {faltas}')
