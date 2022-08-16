'''valor = float(input('Qual o valor da casa? R$ '))
salário = float(input('Qual o seu salário? R$ '))
anos = int(input('Em quantos anos você pretende pagar? '))
prestação = valor / (anos * 12)
minimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(valor, anos))
print('a prestação será de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Empréstimo PODE SER CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')'''

#EXERCICIO37

numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida. Tente novamente.')

#EXERCICIO38

'''n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O primeiro valor é maior.')
elif n2 > n1:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')'''

#EXERCICIO39
'''from datetime import date
atual = date.today().year
nasc = int(input('Qual o seu ano de nascimento? '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Chegou a hora de se alistar ao serviço militar!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para você se alistar ao serviço militar!'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
else:
    saldo = idade - 18
    print('Você já passou {} anos do tempo de alistamento!'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))'''

#EXERCICIO40

'''n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}.'.format(n1, n2, media))

if media < 5.0:
    print('O aluno está REPROVADO')
elif 7 > media >= 5.0:
    print('O aluno está de RECUPERAÇÃO')
else:
    print('O aluno está APROVADO')'''

#EXERCICIO41
'''from datetime import date
atual = date.today().year
ano = int(input('Em que ano você nasceu? '))
idade = atual - ano
print('Você tem {} anos.'.format(idade))

if idade <= 9:
    print('E a sua categoria é a MIRIM')
elif idade <= 14:
    print('E a sua categoria é a INFANTIL')
elif idade <= 19:
    print('E a sua categoria é a JUNIOR')
elif idade <= 25:
    print('E a sua categoria é a SENIOR')
else:
    print('E a sua categoria é a MASTER')'''

#EXERCICIO42
'''r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
if IMC < 18.5:
    print('Você está ABAIXO DO PESO!')
elif 18.5 <= IMC < 25:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')'''

#EXERCÍCIO43

'''altura = float(input('Sua altura: (m) '))
peso = float(input('Seu peso: (kg) '))
IMC = peso / (altura ** 2)
print('Seu IMC é {:.1f}'.format(IMC))

    print('Você está no PESO IDEAL!')
elif 25 <= IMC < 30:
    print('Você está com SOBREPESO!')
elif 30 <= IMC < 40:
    print('Você está com OBESIDADE!')
else:
    print('OBESIDADE MÓRBIDA!')'''

#EXERCÍCIO44

'''valor = float(input('Qual o valor normal do produto? R$'))
print('Qual a forma de pagamento? 
[1] Dinheiro
[2] À vista no cartão
[3] Em até 2x no cartão
[4] Em 3x ou mais no cartão')
pagamento = int(input('Escolha uma opção: '))
if pagamento == 1:
    total = valor - (valor * 10 / 100)
elif pagamento == 2:
    total = valor - (valor * 5 / 100)
elif pagamento == 3:
    total = valor
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(parcela))
elif pagamento == 4:
    total = valor + (valor * 20 / 100)
    totalparc = int(input('Em quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(totalparc, parcela))
else:
    total = 0
    print('OPÇÃO INVÁLIDA! Tente novamente!')
print('O produto de R${:.2f} passa a custar R${:.2f}'.format(valor, total))'''

#EXERCÍCIO45
'''from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura )
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*13)
print('Computador jogou {}.'.format(itens[computador]))
print('Jogador jogou {}.'.format(itens[jogador]))
print('-='*13)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')'''