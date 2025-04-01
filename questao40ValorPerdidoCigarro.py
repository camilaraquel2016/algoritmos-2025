# entrada

anosFuma = int(input('Há quantos anos você fuma? '))
cigarrosPorDia = int(input('Quantos cigarros em média você fuma por dia? '))
valorCarteira = float(input('Qual o valor da carteira? R$'))

# processamento

cigarrosFumadosTotal = anosFuma * 365 * cigarrosPorDia
carteirasFumadas = cigarrosFumadosTotal / 20
valorGastoTotal = carteirasFumadas * valorCarteira

# saida

print(f'Valor total gasto com cigarro: R${valorGastoTotal:.2f}')
