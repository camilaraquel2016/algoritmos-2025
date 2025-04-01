# entrada

numeradorPrimera = int(input('Numerador da primera fração: ')) 
denominadorPrimera = int(input('Denominador da primera fração: ')) 
numeradorSegunda = int(input('Numerador da segunda fração: ')) 
denominadorSegunda = int(input('Denominador da segunda fração: ')) 

# processamento

numeradorResultado = (numeradorPrimera * denominadorSegunda) + (numeradorSegunda * denominadorPrimera) 
denominadorResultado = denominadorPrimera * denominadorSegunda

# saida

print(f'{numeradorPrimera}/{denominadorPrimera} + {numeradorSegunda}/{denominadorSegunda} = {numeradorResultado}/{denominadorResultado}')