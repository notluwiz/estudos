
# Solicitar 2 notas de um aluno e verificar a media
# Media >= 6

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 6:  # True
    print(f'A sua media foi de {media:.2f} e foi aprovado.')

print('Programa continua...')