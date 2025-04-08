# Solicita o preço de uma compra
# valor for superior a 200.00, deve ser concedido um desconto de 10%

valor = float(input('Digite o valor da compra: '))

if valor > 200:
    desc = valor * 0.10
    valor = valor - desc

print(f'Valor final da compra: {valor}')

