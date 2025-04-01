# entrada

quantLatao = float(input('Informe a quantidade de latão em Kg: '))

# processamento 

cobre = 0.7 * quantLatao
zinco = 0.3 * quantLatao

# saida

print(f'Para {quantLatao:.2f} Kg de latão, são necessários {cobre:.2f} Kg de cobre e {zinco:.2f} Kg de zinco')