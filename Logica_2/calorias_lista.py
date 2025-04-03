calorias = []
resposta = ""

while resposta.upper() != 'NÃO':
    caloria = input('Quantas calorias você conseguiu nesta refeição?')
    calorias.append(caloria)
    resposta = input('Você deseja informar as calorias de mais uma refeição?')

total = 0
for caloria in calorias:
    print(f'Nesta refeição foram consumidas {caloria} calorias')
    total = total + caloria

media = total/ len(calorias)
print('Neste dia, houve um consumo médio de {media} calorias por refeição')
