# contador = 0

# while contador < 10:
#     print('Precessando dados')
#     contador += 1
#--------------------------------------------------------------------------------------------------------------------------
# bem_vindo = 0

# while bem_vindo < 5:
#     print('Bem vindo ao buscante')
#     bem_vindo += 1

# for i in range(5):
#     print("Bem-vindo ao Buscante!")
#--------------------------------------------------------------------------------------------------------------------------
# numeros = [10, 20, 30, 40, 50]

# soma = 0
# for numero in numeros:
#     soma += numero

# print(f"A soma total das receitas é: {soma}")

#--------------------------------------------------------------------------------------------------------------------------
# projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

# for projeto in projetos:
#     while projeto == None:
#         print('Projeto inexistente')
#         break
#     print(projeto)

# #--------------------------------------------------------------------------------------------------------------------------

#     projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

# for projeto in projetos:
#     if projeto is None:
#         print("Projeto ausente")
#     else:
#         print(projeto)

#--------------------------------------------------------------------------------------------------------------------------

# livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

# for livro in livros:
#     if livro == "O Hobbit":
#         print(f"Livro encontrado: {livro}")
#         break

#--------------------------------------------------------------------------------------------------------------------------

# estoque = 5
# while estoque > 0:
#     print (f'Venda realizada! Estoque restante: {estoque}')
#     estoque -= 1
    
# print('Estoque esgotado')

#--------------------------------------------------------------------------------------------------------------------------
# segs =[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# for seg in segs:
#     if seg % 2 == 0:
#         print(f'Faltam apenas {seg} segundos- Não perca essa oportunidade!')
#     else:
#         print(f'A contagem continua: {seg} segundos restantes')

# print('Aproveite a promoção agora!')

#--------------------------------------------------------------------------------------------------------------------------
livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

for livro in livros:
    if livro["estoque"] == 0:
        continue
    print(f"Livro disponível: {livro['nome']}")
