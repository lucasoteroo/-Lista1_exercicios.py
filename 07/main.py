'''Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).'''

f= float(input("Informe a quantidade de graus Fahrenheit: "))
celsius =  (f - 32) * 5/9
print("A quantidade informada em graus celsius é", celsius,"°")