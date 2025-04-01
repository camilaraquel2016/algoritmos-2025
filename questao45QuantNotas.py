# entrada

print('-=-=-=-=-=-=-=-Caixa Eletrônico-=-=-=-=-=-=-=-')
print('-----Seja bem-vindo(a) ao sistema de saque-----')
valor = float(input('Qual valor deseja sacar? R$'))

# processamento

notasDe50 = valor // 50
notasDe10 = valor % 50 // 10
notasDe5 = valor % 10 // 5
notasDe1 = valor % 5 // 1

# saida


print('-=-=-Notas a receber-=-=-')
print(f'Notas de R$50: {notasDe50:.0f}\nNotas de R$10: {notasDe10:.0f}\nNotas de R$5: {notasDe5:.0f}\nNotas de R$1: {notasDe1:.0f}')