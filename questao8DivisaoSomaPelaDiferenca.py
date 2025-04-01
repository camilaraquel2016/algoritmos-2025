# entrada

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

# processamento

somaNum = num1 + num2
diferencaNum = num1 - num2
divisaoSomaPelaDiferenca = somaNum / diferencaNum

# saida

print(f'Soma: {num1} + {num2} = {somaNum}\nDiferença: {num1} - {num2} = {diferencaNum}\nDivisão da soma pela diferença dos números: {somaNum} / {diferencaNum} = {divisaoSomaPelaDiferenca:.2f}')
