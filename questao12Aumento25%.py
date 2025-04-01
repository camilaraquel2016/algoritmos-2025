# entrada

salario = float(input('Digite seu salário atual: R$'))

# processamento 

aumento = 0.25 * salario
novoSalario = salario + aumento

# saida

print(f'O salário de R${salario:.2f} com um aumento de 25%, ou seja, R${aumento:.2f} de aumento, passará a ser de R${novoSalario:.2f}')