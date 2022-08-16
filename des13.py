#desafio 13 aula 07

salario = float(input('Qual o seu atual salário? R$'))
aumento = salario + (salario * 15 / 100)
print('Com o aumento de 15%, o seu salário passa a ser R${:.2f}'.format(aumento))