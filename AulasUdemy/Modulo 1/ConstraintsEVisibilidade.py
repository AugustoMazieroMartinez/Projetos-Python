velocidade = 200
local_carro = 90

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1
ultrapassa_limite = velocidade > RADAR_1
radar_range_mais = LOCAL_1 + RADAR_RANGE
radar_range_menos = LOCAL_1 - RADAR_RANGE
multado = local_carro >= radar_range_mais and local_carro <= radar_range_menos
if ultrapassa_limite and multado:
    print('Velocidade do carro passou o limite de velocidade')
    print('Carro multado em radar 1')
else:
    print('Nenhum problema aqui')