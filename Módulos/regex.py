#. - QUalquer caractere
#\d - qualquer digito(0 - 9)
#\D - Qualquer caractere que não seja um digito
#\w - qualquer caractere alfanumérico
#\W - Qualquer caractere que não seja alfanumérico
#\s - Qualquer espaço em branco
#\S - QUalquer caractere que não seja espaço em branco
#[abc] - Corresponde a qualquer caractere 'a', 'b' ou 'c'
#[^abc] - Corresponde a qualquer caractere que não seja 'a', 'b' ou 'c'
#[a-z] - Corresponde a qualquer caractere de 'a' a 'z' (minúsculas)
#[A-Z] - Corresponde a qualquer caractere de 'A' a 'Z' (maiúsculas)
#[0-9] - Corresponde a qualquer dígito (0-9)
#[a-zA-Z] - Corresponde a qualquer letra, maiúscula ou minúscula
#* - Corresponde a 0 ou mais ocorrências do padrão anterior
#+ - Corresponde a 1 ou mais ocorrências do padrão anterior
#? - Corresponde a 0 ou 1 ocorrência do padrão anterior
#{n} - Corresponde exatamente a n ocorrências do padrão anterior
#{n,} - Corresponde a n ou mais ocorrências do padrão anterior
#{n,m} - Corresponde entre n e m ocorrências do padrão anterior
# Função     | Descrição                                                                 | Exemplo                                                         | Retorno
# -----------|---------------------------------------------------------------------------|------------------------------------------------------------------|-----------------------------
# search     | Procura por um padrão em qualquer parte da string. Retorna o primeiro     | re.search(r"\d+", "Há 1234 alunos")                             | Retorna '1234'
#            | resultado encontrado.                                                    |                                                                  |

# match      | Verifica se o padrão corresponde ao início da string.                    | re.match("abc", "abcdef")                                       | Retorna um match com 'abc'

# findall    | Retorna todas as ocorrências do padrão em uma lista.                     | re.findall(r"\d+", "Eu tenho 3 gatos e 2 cachorros")            | Retorna a lista ['3', '2']

# sub        | Substitui ocorrências do padrão por uma string.                          | re.sub(r"\d", "#", "Meu número é 1234")                         | Retorna 'Meu número é ####'
import re
import re

# texto = "Entre em contato pelo email support@example.com"

# padrao_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# resultado = re.search(padrao_email, texto)

# if resultado:
#     print("Email encontrado:", resultado.group())
# else:
#     print("Nenhum email encontrado.")

# produto = input('Digite o nome do produto: ')

# produto_padrao = produto.strip().lower()
# print(produto_padrao)

# nome = input('Digite o nome do cliente: ')
# cidade = input('Digite a cidade do cliente: ')


# print(f'Olá {nome}! Bem vinda ao sistema da cidade de {cidade}.')

# texto = input("Digite a palavra-chave: ")  
# primeiras = texto[:3]
# ultimas = texto[-3:]
# print(f"Primeiras: {primeiras}")
# print(f"Últimas: {ultimas}")

# url = input("Digite a URL para validação: ") 
# if url.startswith("https://") and url.endswith(".com"):
#     print("URL válida!")
# else:
#     print("URL inválida!")



# texto = input("Digite a descrição da receita: ")  
# numero = re.findall(r'\d+', texto)[0]  
# print(f"O número da receita é: {numero}")

import re

cpf = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")  
padrao = r'\d{3}\.\d{3}\.\d{3}-\d{2}'

if re.search(padrao, cpf):
    print("O CPF está no formato correto.")
else:
    print("O CPF está no formato incorreto.")
