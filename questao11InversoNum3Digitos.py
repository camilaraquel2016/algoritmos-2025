# entrada 

num = int(input('Digite um número (100 a 999): '))

# processamento

centena = num // 100
dezena = (num % 100) // 10
unidade = num % 10 
numInverso = unidade * 100 + dezena * 10 + centena 

# saida

print(f'Inverso do número {num} = {numInverso} ')
