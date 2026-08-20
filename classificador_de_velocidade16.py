velocidade = int(input('Digite a velocidade. '))
if velocidade > 120:
    print('Velocidade muito alta')
elif velocidade >= 81:
    print('Velocidade alta')
elif velocidade >= 41:
    print('Velocidade normal')
else:
    print('Velocidade baixa')
