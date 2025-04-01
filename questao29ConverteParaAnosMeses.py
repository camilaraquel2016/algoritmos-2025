# entrada 

mesesTotais = int(input('Digite um período em meses: '))

# processamento

anos = mesesTotais // 12
meses = mesesTotais % 12

# saida

print(f'{mesesTotais} meses equivale a {anos} ano(s) e {meses} meses')