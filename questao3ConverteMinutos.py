# entrada 

minutosTotais = int(input('Digite o tempo em minutos: '))

# processamento

horas = minutosTotais // 60
minutos = minutosTotais % 60

# saida

print(f'{minutosTotais} minutos equivale a {horas} hora(s) e {minutos} minuto(s)')