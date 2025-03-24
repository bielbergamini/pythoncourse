# try:
#     numero = (int(input ('Digite um numero inteiro: ')))

#     if numero % 2 == 0:
#         print('Par')
#     else:
#         print('Impar')

# except ValueError:
#     print('Valor inválido! Por favor, digite um número inteiro.')





# try:
#     dia = 0.11
#     tarde = 12.17
#     noite = 18.23

#     hora_do_dia = float(input('Digite que horas são: '))

#     if dia <= hora_do_dia <= tarde:
#         input('Bom dia!')
#     elif tarde <= hora_do_dia <= noite:
#         print('Boa tarde!')
#     else:
#         print('Boa noite!')

# except ValueError:
#     print('Valor inválido')


nome = input(f'Digite seu nome: ')
caracteres = len(nome)

if len(nome) <= 4:
    input('Seu nome é muito curto')
elif len(nome) == 5 or len(nome) == 6:
    print('Seu nome é normal')
elif len(nome) > 6 :
    print('Seu nome é muito grande')











