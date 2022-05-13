'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''


s= str(input("Informe seu gênero: (homem ou mulher): ")).upper() 

if s == "HOMEM" :
  hh=float(input("Gentileza informar sua altura: "))
  pesoideal_homem= (72.7*hh) - 58
  print("Seu peso ideal para sua altura é", pesoideal_homem, "kg")

elif s == "MULHER":
  hm= float(input("Gentileza informar sua altura: "))
  pesoideal_mulher= (62.1*hm) - 44.7
  print("Seu peso ideal para sua altura é", pesoideal_mulher, "kg")
