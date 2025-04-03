lista = ['1']

lista.insert(1, 3)

#Inserindo novos elementos
lista.append('Teste de inserção')

#Mostrando a lista inteira
print(lista)

#Mostrando elemento pelo índice
print(lista[2])


#Exibindo com loop
for valor in lista:
    print(valor)


#removendo
lista.pop()
print(lista)
lista.remove(1)
print(lista)



#tamanho da lista
print(len(lista))
