#Faça um Programa que recebe um tempo em dias, horas e minutos, e, produz como saída esse tempo total em minutos.

dias= int(input("Informe a quantidade em dias: "))
horas=int(input("Agora a quantidade em horas: "))
minutos= float(input("Por fim informe a quantidade em minutos: "))

minutostotal=(dias*1440) + (horas*60) + minutos

print(f"O resultado em minutos é: {minutostotal}")