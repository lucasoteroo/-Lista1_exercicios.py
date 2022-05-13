'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do stado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.'''

pesolimite=50
peso_peixes= float(input("Quantos quilos de peixes foram pescados? "))
if peso_peixes > pesolimite :
  excesso = peso_peixes - pesolimite
  multa = 4 * excesso
  print("Você pescou", excesso,"kg além do permitido, com isso o valor da multa por esse excesso será de:",multa,"reais")

else: 
  print("Você não pesou além do permitido, com isso não pagará multa. ")
