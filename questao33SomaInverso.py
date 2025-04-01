# entrada

num = int(input('Digite um número de 3 dígitos: '))

# processamento

centena = num // 100
dezena = num % 100 // 10
unidade = num % 10
numInverso = unidade * 100 + dezena * 10 + centena
soma = num + numInverso

# saida

print(f'Soma: {num} + {numInverso} = {num + numInverso}')
