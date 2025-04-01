# entrada
 
x1 = float(input('x1: '))
y1 = float(input('y1: '))
x2 = float(input('x2: '))
y2 = float(input('y2: '))

# processamento

distanciaDosPontos = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)

# saida

print(f'A distância entre os pontos ({x1}, {y1}) e ({x2}, {y2}) é {distanciaDosPontos:.2f}')