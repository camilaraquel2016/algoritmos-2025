# entrada

print('-=-Loja você bonita-=-')
valorProduto = float(input('Qual valor do produto? R$'))

# processamento

parcela = valorProduto // 3
entrada = valorProduto - 2 * parcela

# saida 

print(f'Para um produto de R${valorProduto:.2f}, será necessário uma entrada no valor de R${entrada:.2f} e mais 2 parcelas de R${parcela:.2f} cada uma')
