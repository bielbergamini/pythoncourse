# Intepolação básica de strings
# s - strings
# d e i - int
# f - float 
# x e X - Hexadecimal (ABCDEF0123456789)
# (Caractere)(><^)(quantidade)
# > - Esquerda
# < - Direita
# ^ - Centro
# Sinal - + ou -
# Ex.: 0>-100,.1f
# Conversion flags - !r !s !a

nome = 'Gabriel'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print (variavel)
print ('O Hexadecimal de %d é %08X' % (1500, 1500))

variavel = 'ABC'
print(f'{variavel: >10}') #preenche a formatação para a direção escolhida
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.631826371638:.1f}')
