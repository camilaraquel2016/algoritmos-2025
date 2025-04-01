# entrada 

metrosTotais = float(input('Digite uma medida em metros: '))

# processamento

km = metrosTotais // 1000
metros = metrosTotais % 1000

# saida

print(f'{metrosTotais} metros equivale a {km} km e {metros} metro(s)')