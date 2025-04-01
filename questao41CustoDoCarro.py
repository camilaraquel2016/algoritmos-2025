# entrada

custoDeFabrica = float(input('Qual o custo de fábrica? R$'))
percentagemDistri = float(input('Qual a percentagem do distribuidor? '))
percentagemImposto = float(input('Qual a percentagem do imposto? '))

# processamento

valorDistribuidor = percentagemDistri / 100 * custoDeFabrica
valorImposto = percentagemImposto / 100 * custoDeFabrica
custoConsumidor = custoDeFabrica + valorDistribuidor + valorImposto

# saida

print(f'Valor final do carro após aplicações das percentagem de distribuidor e impostos: R${custoConsumidor:.2f}')
