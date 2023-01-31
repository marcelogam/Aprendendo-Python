altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
area = altura * largura

print('A parde tem uma area de {}'.format(area)) 
print('Sabendo que cada litro de tinta pinta um total de 2m^2, para pintar toda esta parede, sera necessario um total de {} litros de oleo'.format(area//2+1)) 