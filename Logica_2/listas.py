lista = ['1']

lista.insert(1, 3)
lista.append('Teste de inserção')

print(lista[2])

for valor in lista:
    print(valor)

lista.pop()
print(lista)
lista.remove(1)
print(lista)
