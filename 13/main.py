'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao Imposto de renda (-11%)
quanto pagou ao INSS (-8%).
quanto pagou ao sindicato (-5%).
o salário líquido (Salário Bruto - Descontos = Salário Líquido)'''

horas=float(input("Informe quantas horas você trabalhou nesse mês: "))
valor_hora= float(input("Quanto vale sua hora de trabalho? "))

salario_bruto = valor_hora * horas
desconto_imposto = salario_bruto/100* 11
desconto_inss= salario_bruto/100 *8
desconto_sindicato = salario_bruto/100*5
desconto_total = desconto_imposto + desconto_inss + desconto_sindicato
salario_liquido = salario_bruto - desconto_total

print ("Seu salário sem descontos é de", salario_bruto,"reais")
print("__________________________________________________________")
print ("Foi descontado do seu sálario bruto 11% para o imposto de renda, isso é igual á", desconto_imposto,"reais")
print ("Foi descontado do seu sálario bruto 8% para o INSS, isso é igual á", desconto_inss,"reais")
print ("Foi descontado do seu sálario bruto 5% para o sindicato, isso é igual á", desconto_sindicato,"reais")
print ("________________________________________________________")
print ("Seu salário com descontos é de", salario_liquido,"reais")


