# entrada

numBin = int(input('Digite um número de 4 dígitos na sua forma binária: '))

# processamento 

milhar = numBin // 1000
centena = (numBin % 1000) // 100
dezena = (numBin % 100) // 10
unidade = numBin % 10
numDecimal = milhar * 8 + centena * 4 + dezena * 2 + unidade * 1 

# saida

print(f'Número na base binária: {numBin}\nNúmero na base decimal: {numDecimal}')