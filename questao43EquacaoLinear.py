# entrada

a = float(input('Coeficiente A: '))
b = float(input('Coeficiente B: '))
c = float(input('Coeficiente C: '))
d = float(input('Coeficiente D: '))
e = float(input('Coeficiente E: '))
f = float(input('Coeficiente F: '))

# processamento

valorDeX = (c * e - b * f) / (a * e - b * d)
valorDeY = (a * f - c * d) / (a * e - b * d)

# saida

print(f'Valor de x: {valorDeX:.2f}\nValor de y: {valorDeY:.2f}')


