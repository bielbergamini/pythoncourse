# Importação do OrderedDict
from collections import OrderedDict
# Criação
dicionario_ordenado = OrderedDict()
# Adicionando chaves e valores
dicionario_ordenado['NOME'] = 'Iphone'
dicionario_ordenado['MARCA'] = 'Apple'
dicionario_ordenado['MODELO'] = 'XR'
# Percorrendo para verificar a ordem
for chave, valor in dicionario_ordenado.items():
    print(f'{chave} -- {valor}')
# Alterando um item
print()
dicionario_ordenado['MARCA'] = 'Maça'

# Percorrendo para verificar a ordem
for chave, valor in dicionario_ordenado.items():
    print(f'{chave} -- {valor}')


# Removendo um item
dicionario_ordenado.pop('MARCA')
print()

# Percorrendo para verificar a ordem
for chave, valor in dicionario_ordenado.items():
    print(f'{chave} -- {valor}')

# Reinserindo um item na lista
dicionario_ordenado['MARCA'] = 'Apple'
print()

# Percorrendo para verificar a ordem 
for chave, valor in dicionario_ordenado.items():
    print(f'{chave} -- {valor}')


