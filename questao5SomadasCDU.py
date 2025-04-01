# entrada

num = int(input('Digite um número de 3 dígitos: '))

# processamento

centena = num // 100
dezena = (num % 100) // 10
unidade = (num % 100) % 10
somaDosElementos = centena + dezena + unidade

# saida

print(f'{centena} + {dezena} + {unidade} = {centena + dezena + unidade}')
