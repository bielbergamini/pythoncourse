import sys

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome == "" or idade == "":
    print('Desculpe, você deixou campos vazios')
    sys.exit()
    print('Desculpe, você deixou campos vazios')
else:
    print(f'Seu nome é {nome}, Seu nome invertido é: {nome[::-1]}')
    if nome == " ":
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')

print(f'Seu nome tem {len(nome)} letras')
print(f'A primeira letra do seu nome é: {nome[0]}')
print(f'A ultima letra do seu nome é: {nome[-1]}')

