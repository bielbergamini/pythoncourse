nome = input('Digite seu nome: ')
peso = int(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
idade = int(input('Digite sua idade: '))
peso_minimo = 70 
idade_minima = 18


if peso < peso_minimo and idade < idade_minima:
    print('Você não atende nenhum dos requisitos para ser um doador')
elif idade < idade_minima:
    print('Você não tem idade ideal para doar')
elif peso < peso_minimo:
    print('Você não tem o peso ideal para doar')
else:
    print('Doação liberada!')
