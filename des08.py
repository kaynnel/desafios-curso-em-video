#desafio 8 aula 07

medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('A medida de {} corresponde a '.format(medida))
print('{}cm, {}mm, {}dm, {}dam, {}hm, {}km'.format(cm, mm, dm, dam, hm, km))