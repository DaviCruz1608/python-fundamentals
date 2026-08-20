valor = float(input('Digite o valor da compra:'))
if valor >= 200:
    desconto_1 = valor * 0.20
    valor_final = valor - desconto_1
    print('Desconto de 20%, ou seja: ', desconto_1)
    print('Valor final: ', valor_final)
elif valor >= 100:
    desconto_2 = valor * 0.10
    valor_final2 = valor - desconto_2
    print('Desconto de 10%, ou seja: ', desconto_2)
    print('Valor final: ',valor_final2)
elif valor >= 50:
    desconto_3 = valor * 0.05
    valor_final3 = valor - desconto_3
    print('Desconto de 5%, ou seja: ', desconto_3)
    print('Valor final: ', valor_final3)
else:
    print('Sem desconto')

