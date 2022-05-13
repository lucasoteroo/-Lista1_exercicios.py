'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre separadamente:
o produto do dobro do primeiro com metade do segundo.
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.'''

inteiro= int(input("Informe o primeiro número inteiro: "))
inteiro2= int(input("Informe o segundo número inteiro: "))
real= float(input("Informe o número real: "))

total1= (inteiro *2) * (inteiro2/2)
total2= (inteiro*3) + real
total3= real**3

print("O produto do primeiro com metade do segundo:", total1)
print("a soma do triplo do primeiro com o terceiro:", total2)
print("o terceiro elevado ao cubo:", total3)