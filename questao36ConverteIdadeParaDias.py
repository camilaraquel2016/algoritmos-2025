# entrada 
print('Digite a idade em ')
anosIdade = int(input('anos: '))
mesesIdade = int(input('meses: '))
diasIdade = int(input('dias: '))

# processamento

diasTotaisDaIdade = anosIdade * 365 + mesesIdade * 30 + diasIdade

# saida

print(f'{anosIdade} ano(s), {mesesIdade} mes(es) e {diasIdade} dia(s) equivale a {diasTotaisDaIdade} dias ao todo')