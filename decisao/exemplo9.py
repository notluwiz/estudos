# Calculadora Basica

a = float(input('Primeiro numero: '))
b = float(input('Segundo numero: '))

print('1 - Soma \n2 - subtraçao \n3 - Multiplicaçao \n4 - Divisao')

opcao = int(input('Escolha uma opçao: '))

if opcao == 1:
    print(f'Soma no valor de {a + b}')
elif opcao == 2:
    print(f'Subtraçao no valor de {a - b}')
elif opcao == 3:
    print(f'multiplicaçao no valor de {a * b}')
elif opcao == 4:
    print(f'Divisao no valor de {a / b}')
else:
    print('Opçao invalida')