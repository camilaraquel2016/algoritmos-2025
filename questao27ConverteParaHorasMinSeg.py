# entrada

segundosTotais = int(input('Digite um valor em segundos: '))

# processamento 

horas = segundosTotais // 3600
minutos = segundosTotais % 3600 // 60
segundos = segundosTotais % 60

# saida

print(f'{segundosTotais} segundos equivale a {horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s)')
