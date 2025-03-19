velocidade = 61
local_carro = 101

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

carro_multado = local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1
carro_liberdado = local_carro = (LOCAL_1 + RADAR_RANGE) and velocidade <= RADAR_1

if carro_multado:
    print("Você foi multado") 
else:
    print("Você foi liberado")
