# Calculadora Basica

a = float(input('Primeiro numero: '))
b = float(input('Segundo numero: '))

print('1 - Soma \n2 - subtraçao \n3 - Multiplicaçao \n4 - Divisao')

opcao = int(input('Escolha uma opçao: '))

match opcao:
    case 1:
        print(f'Soma no valor de {a + b}')
    case 2:
        print(f'Subtraçao no valor de {a - b}')
    case 3:
        print(f'Multiplicaçao no valor de {a * b}')
    case 4:
        print(f'Divisao no valor de {a / b}')
    case _:
        print('Opçao invalida')