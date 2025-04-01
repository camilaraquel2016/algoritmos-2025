# entrada

idadeEmDiasTotais = int(input('Qual sua idade expressa em dias? '))

# processamento

anos = idadeEmDiasTotais // 365
meses = idadeEmDiasTotais % 365 // 30
dias = (idadeEmDiasTotais % 365) % 30

# saida

print(f'{idadeEmDiasTotais} dias equivale a {anos} ano(s), {meses} mes(es) e {dias} dia(s)')
