# entrada

num = int(input('Digite um número de 4 dígitos: '))

# processamento

milhar = num // 1000
centena = num % 1000 // 100
dezena = num % 100 // 10
unidade = num % 10
somaDosElementos = milhar + centena + dezena + unidade

# processamento

print(f'Soma dos elementos: {milhar} + {centena} + {dezena} + {unidade} = {somaDosElementos}')

