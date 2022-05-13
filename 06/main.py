'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''

ganho_hora= float(input("Informe quanto você ganha por hora: "))
horas_trab = int(input("Informe a quantidade de horas trabalhadas no mês: "))

salario = ganho_hora* horas_trab
print("Seu salário do mês é:",salario, "reais")