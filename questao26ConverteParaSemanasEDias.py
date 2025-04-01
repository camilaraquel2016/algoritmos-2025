# entrada

diasTotais = int(input('Digite um valor em dias: '))

# processamento

semanas = diasTotais // 7
dias = diasTotais % 7

# saida

print(f'{diasTotais} dias equivale a {semanas} semana(s) e {dias} dia(s)')