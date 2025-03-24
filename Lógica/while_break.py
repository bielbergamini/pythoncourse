# while (enquanto)
# Executa uma ação enquanto uma condição for verdadeira
#-------------------------------------------------------------------------
# condicao = True

# while condicao:
#     nome = input('Digite seu nome: ')
#     print(f'Seu nome é {nome}')

#     if nome == 'sair':
#         break
#     print('Fim')

qtd_linhas = 50
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1 
    print(linha)

    while coluna <= qtd_colunas:
        print()
        coluna += 1
    linha += 1     
      
    linha += 1
    
    print('Acabou')