# CÓDIGO SEM FUNÇÕES

# # solicitar distância e tempo
# distancia = float(input('Digite a distância percorrida'))
# tempo = float(input('Digite o tempo da viagem'))
# velocidade_media = distancia / tempo
# # exibir o resultado
# print(f'A velocidade média é: {velocidade_media}') 

#-----------------------------------------------------------------------------
#UTILIZANDO FUNÇÕES
def calcular_velocidade_media():
    velocidade_media = distancia / tempo
# exibir o resultado
    print(f'A velocidade média é: {velocidade_media}') 


distancia = float(input('Digite a distância percorrida: '))
tempo = float(input('Digite o tempo da viagem: '))
calcular_velocidade_media()



