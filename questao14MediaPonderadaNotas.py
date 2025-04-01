# entrada

nota1 = float(input('Primeira nota: '))
peso1 = float(input('Peso da primera nota: '))
nota2 = float(input('Segunda nota: '))
peso2 = float(input('Peso da segunda nota: '))
nota3 = float(input('Terceira nota: '))
peso3 = float(input('Peso da terceira nota: '))

# processamento

mediaPonderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

# saida

print(f'Média ponderada das notas: {mediaPonderada:.2f}')
