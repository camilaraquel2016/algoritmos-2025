# entrada

horasTotais = int(input('Digite um valor em horas: '))

# processamento 

semanas = horasTotais // 168
dias = horasTotais % 168 // 24
horas = horasTotais % 24

# saida

print(f'{horasTotais} horas equivale a {semanas} semana(s), {dias} dia(s) e {horas} hora(s)')