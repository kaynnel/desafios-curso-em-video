#exercício 28
'''from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador "PENSAR"
print('-=-' * 10)
print('Pense em um número de 0 a 5...')
print('-=-' * 10)
jogador = int(input('Em que número você pensou? ')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(1)
if jogador == computador:
    print('Parabéns! Você acertou!')
else:
    print('Você errou! Eu pensei no número {}'.format(computador))'''

#exercício 29
'''velocidade = float(input('Qual a velocidade do carro? '))
limite = 80
multa = (velocidade-80) * 7
if velocidade > limite:
    print('Você ultrapassou {}km/h. Você foi multado em R$ {:.2f}.'.format(limite, multa))
else:
    print('Você respeitou o limite de velocidade imposto!')'''

#exercício 30
'''n = int(input('Escolha um número: '))
resultado = n % 2
if resultado == 0:
    print('O número {} é PAR!'.format(n))
else:
    print('O numéro {} é IMPAR!'.format(n))'''

#exercício 31
'''viagem = int(input('Qual é a distância da viagem? '))
print('Você está prestes a começar uma viagem de {:.1f} km.'.format(viagem))
if viagem <= 200:
    preco = 0.50 * viagem
else:
    preco = 0.45 * viagem
print('E o preço da sua passagem será de R$ {:.2f}'.format(preco))'''

#exercício 32
'''from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0 :
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano BISSEXTO.'.format(ano))
else:
    print('{} não é um ano BISSEXTO.'.format(ano))'''

#exercício 33
'''a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
    
print('O maior número foi {}.'.format(maior))
print('O menor número foi {}.'.format(menor))'''

#exercício 34
'''salario = float(input('Qual é o salário do funcionário? '))
if salario => 1250:
    aumento1 = salario + (salario * 10/100)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, aumento1))
else:
    aumento2 = salario + (salario * 15/100)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, aumento2))'''

#exercício 35
#comprimento de 3 retas que podem ou não formar um triângulo
print('='*24)
print('Analisador de Triângulos')
print('='*24)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
