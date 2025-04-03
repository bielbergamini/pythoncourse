from collections import defaultdict

dicionario_lista = defaultdict(list)
dicionario_lista['PRODUTO'] = 'Macbook Pro'
dicionario_lista['MARCA'] = 'Apple'

def funcao_exemplo():
    return 'INEXISTENTE'
dicionario_funcao = defaultdict(list)
dicionario_funcao['PRODUTO'] = 'Macbook Pro'
dicionario_funcao['MARCA'] = 'Apple'

print (dicionario_funcao)
print(dicionario_lista['PREÇO'])
print(dicionario_lista)

# Criação de dicionário com uma funcção lambda
dicionario_lambda = defaultdict(lambda: 'Não disponível')
dicionario_lambda['PRODUTO'] = 'Macbook Pro'
dicionario_lambda['MARCA'] = 'Apple'

print(dicionario_lambda)
print(dicionario_lambda['PREÇO'])
print(dicionario_lambda)

