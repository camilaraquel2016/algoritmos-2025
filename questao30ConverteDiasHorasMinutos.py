# entrada

minutosTotais = int(input('Digite um valor em minutos: '))

# processamento

dias = minutosTotais // 1440
horas = minutosTotais % 1440 // 60
minutos = minutosTotais % 60

# saida

print(f'{minutosTotais} minutos equivale a {dias} dia(s), {horas} hora(s) e {minutos} minuto(s)')
