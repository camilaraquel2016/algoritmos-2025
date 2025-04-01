#entrada 

velocidadeMetrosPorSeg = float(input('Qual a velocidade em m/s? '))

# processamento

velocidadeKmPorH = velocidadeMetrosPorSeg * 3.6

# saida

print(f'{velocidadeMetrosPorSeg} m/s equivale a {velocidadeKmPorH:.2f} Km/h')