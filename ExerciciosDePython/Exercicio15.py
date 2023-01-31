dias = int(input('Por quantos dias o carro foi alugado: '))
quilometros = float(input('Quntos Km foi rodado: '))
preco = (dias * 60) + (quilometros * 0.15)

print('O total ficou em: R${:.2f}'.format(preco))