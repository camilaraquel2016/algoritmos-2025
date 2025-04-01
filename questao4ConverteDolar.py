# entrada

valorDoDolar = float(input('Qual o valor do dólar atualmente? '))
valorEmDolar = float(input('Qual o valor em dólar? '))

# processamento

valorEmReal = valorEmDolar * valorDoDolar

# saida

print(f'{valorEmDolar:.2f} dólares equivale a {valorEmReal:.2f} reais')