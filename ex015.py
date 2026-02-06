d = float(input('Quatos dias alugados? '))
km = float(input('Quantos km rodados? '))
v = 60 * d + 0.15 * km
print('O total a pagar é de R${:.2f}'.format(v))