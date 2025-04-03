# Função para calcular a velocidade média
def calcular_velocidade_media(distancia:float, tempo:float, unidade_medida='km/h'):
    if tempo == 0:
        return 0
    velocidade_media = distancia / tempo
    return f'{velocidade_media} {unidade_medida}'

# Função para converter a temperatura
def converter_temperatura (temperatura:float, unidade_medida='celsius'):
    if unidade_medida =='celsius':
        return temperatura * 1.8 + 32
    elif unidade_medida == 'fahrenheit':
        return(temperatura - 32) / 1.8
    else:
        return 0
    

def exibir_menu():
    """Função para exibir um menu"""
    print('MENU')
    print('1 - Calcular a velocidade média ')
    print('2 - Converter a temperatura')
    print('3 - Sair')



def aluno_de_fisica():
    op = 0
    while op != 3:
        exibir_menu()
        op = int(input('Informe a opção desejada: '))
        if op == 1:
            distância_percorrida = int(input('Informe a distância: '))
            tempo_viagem = int(input('Informe o tempo da viagem: '))
            medida = input('Informe a unidade de medida: ')
            print(f'A velocidade média é {calcular_velocidade_media(distância_percorrida, tempo_viagem, medida)}')
        elif op == 2:
            temp = float(input('Informe a temperatura: '))
            unid_medida = input('Informe a unidade de medida: ')
            print(f'A temperatura atual é {converter_temperatura(temp, unid_medida)}')
        elif op == 3:
            print('Saindo...')
            break
        else:
            print('Opção inválida')



print(exibir_menu.__doc__)







