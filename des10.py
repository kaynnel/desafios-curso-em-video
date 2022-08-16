#desafio 10 aula 07

reais = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = reais / 4.69
print('Com R${:.2f} você pode comprar U${:.2f}'.format(reais, dolar))