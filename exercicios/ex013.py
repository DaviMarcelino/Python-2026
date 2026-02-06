s = float(input('Qual o salário de funcionário? R$'))
a = s + s * 15/100
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(s,a))