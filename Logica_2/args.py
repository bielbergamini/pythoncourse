# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

# def soma (*args):
#     total = 0
#     for numero in args:
#         print('Total', total)
#         total += numero 
#         print('Total', total)
#     print(total)

#     soma(1, 2, 3, 4, 5, 6)

def exibe_promocao(*clientes):
    for cliente in clientes:
        print(f'Olá {cliente} ! O item X está em promoção')

    
exibe_promocao('Gabriel', 'Bianca')