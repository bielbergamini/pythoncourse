# Operadores lógicos
# and (e) or (ou) not (não)
# and - todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressão inteira sera avaliada naquele valor
# São considerados false
# 0 0.0 '' False
#Também existe o tipo None que é usado para representar um não valor
# and: todas as condições precisam ser verdadeiras
# or: retorna verdadeiro se pelo menos uma das condições for verdadeira


#------------------------------------------------------------------------------------------------------------------------------------------------

# entrada = input ('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'


# if (entrada == 'E' or 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

#-------------------------------------------------------------------------------------------------------------------------------------------------

# macas = input('Digite a quantidade de maçãs vendidas: ')
# banana = input('Digite a quantidade de bananas vendidas: ')


# if macas > banana:
#     print('As maçãs tiveram mais vendas!')
# elif banana > macas:
#     print('As bananas tiveram mais vendas!')
# else:
#     print('As duas frutas venderam a mesma quantidade')
#-------------------------------------------------------------------------------------------------------------------------------------------------

# diaA = int(input('Informe os dias para a atividade A: '))
# diaB = int(input('Informe os dias para a atividade B: '))
# diaC = int(input('Informe os dias para a atividade C: '))

# resultado = diaA + diaB + diaC

# if resultado > 0:
#     print(f'Tempo total das atividade: {resultado}')
# else:
#     print('Os dias não podem ser negativos.')

#-------------------------------------------------------------------------------------------------------------------------------------------------

# temperatura = int(input('Digite a temperatura atual: '))

# if temperatura > 25:
#     print('Alerta! Temperatura acima do permitido.')
# elif temperatura == 25:
#     print('Alerta! Temperatura limite!')
# else:
#     print('Temperatura agradável')

#-------------------------------------------------------------------------------------------------------------------------------------------------

# peso = int(input('Digite seu peso (Kg): '))
# altura = float(input('Digite sua altura (m): '))

# IMC = peso / (altura ** 2)

# if IMC < 18.5:
#     print('Você está abaixo do peso')
# elif 18.5 <= IMC < 25:
#     print('Seu peso está normal')
# elif IMC >= 25:
#     print('Você está acima do peso')
# else : 
#     print('Digite um valor válido')

# peso = float(input("Digite seu peso (kg): "))
# altura = float(input("Digite sua altura (m): "))

# imc = peso / (altura ** 2)
# print(f"Seu IMC é: {imc:.2f}")

# if imc < 18.5:
#     print("Você está abaixo do peso.")
# elif imc < 25:
#     print("Você está com peso normal.")
# else:
#     print("Você está acima do peso.")

#-------------------------------------------------------------------------------------------------------------------------------------------------

# despesa = float(input('Digite o total das despesas do mês(R$): '))

# if despesa > 3000.00:
#     print('Atenção! Você ultrapassou o limite desse mês!')
# else:
#     print('Você está dentro do limite de despesas')

#-------------------------------------------------------------------------------------------------------------------------------------------------

# hora_atual = int(input("Digite a hora atual (formato 24 horas): "))

# if 8 <= hora_atual < 18:
#     print("Acesso permitido.")
# else:
#     print("Acesso negado.")
#-------------------------------------------------------------------------------------------------------------------------------------------------

# nota1 = int(input('Digite a nota 1: '))
# nota2 = int(input('Digite a nota 2: '))
# nota3 = int(input('Digite a nota 3: '))

# media_final = (nota1 + nota2 + nota3) / 3
# print(f'Sua média foi: {media_final}')

# if media_final >= 7:
#     print('Aprovado!')
# elif 5 <= media_final < 7:
#     print('Recuperação')
# else:
#     print('Reprovado')

#-------------------------------------------------------------------------------------------------------------------------------------------------

# km = int(input('Digite a distância percorrida: '))

# if km <= 100:
#     print('10R$')
# elif 100 < km <= 200:
#     print('20R$')
# else:
#     print('30R$')

#-------------------------------------------------------------------------------------------------------------------------------------------------

# hora = int(input('Digite um número inteiro: '))

# if hora % 2 == 0:
#     print('O número é par')
# else:
#     print('O número é impar')
#-------------------------------------------------------------------------------------------------------------------------------------------------

renda = float(input("Digite o valor da sua renda mensal: "))
parcela = float(input("Digite o valor da parcela desejada: "))

if renda > 2000 and parcela <= 0.3 * renda:
    print("Empréstimo aprovado!")
elif renda <= 2000:
    print("Empréstimo negado: renda insuficiente.")
else:
    print("Empréstimo negado: parcela acima de 30% da renda.")









