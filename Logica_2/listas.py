# lista = ['1']

# lista.insert(1, 3)

# #Inserindo novos elementos
# lista.append('Teste de inserção')

# #Mostrando a lista inteira
# print(lista)

# #Mostrando elemento pelo índice
# print(lista[2])


# #Exibindo com loop
# for valor in lista:
#     print(valor)


# #removendo
# lista.pop()
# print(lista)
# lista.remove(1)
# print(lista)



# #tamanho da lista
# print(len(lista))



# lista_compras = [
#     'Arroz',
#     'Feijão',
#     'Carne',
#     'Alface'
# ]

# compra = input('Digite o item que você quer verificar: ')
                                                                                                                            
# if compra in lista_compras:
#     print('Este item já está na lista')
# else:
#     print('Você precisa comprar este item, adicione-o na lista')

# notas = input('Digite as notas: ')
# lista = [int(x.strip()) for x in notas.split(',')]
# lista.sort()

voluntarios = []
# print(lista)
while True:
    nomes = input('Digite o nome do voluntario (ou "sair" para encerrar): ')
    lista = [str(x.strip()) for x in nomes.split(',')]
    if nomes == 'sair':
        print('Você saiu')
        break 
    voluntarios.append(nomes)

print("\nVoluntários registrados:", voluntarios)


# +---------------------+----------------------------------------+
# | COMANDO             | FUNÇÃO                                 |
# +---------------------+----------------------------------------+
# | append(x)           | Adiciona x no final da lista           |
# | insert(i, x)        | Insere x na posição i                  |
# | extend(lista2)      | Junta lista2 à lista atual             |
# | remove(x)           | Remove o primeiro x encontrado         |
# | pop()               | Remove o último item                   |
# | pop(i)              | Remove item da posição i               |
# | clear()             | Esvazia a lista                        |
# | sort()              | Ordena a lista (crescente)             |
# | sorted(lista)       | Retorna nova lista ordenada            |
# | reverse()           | Inverte a ordem da lista               |
# | count(x)            | Conta ocorrências de x                 |
# | index(x)            | Retorna índice do primeiro x           |
# | x in lista          | Verifica se x está na lista            |
# | len(lista)          | Retorna quantidade de itens            |
# | lista.copy()        | Retorna uma cópia da lista             |
# | lista[a:b]          | Fatiamento (do índice a ao b-1)        |
# +---------------------+----------------------------------------+



