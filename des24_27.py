'''cidade = str(input('Qual o nome da cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')'''

'''nome = str(input('Qual seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))'''

'''frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))'''

n = str(input('Digite seu nome completo: ')).upper().strip()
nome = n.split()
print('O seu primeiro nome é {}.'.format(nome[0]))
print('O seu último nome é {}.'.format(nome[len(nome)-1]))


