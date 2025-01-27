#Atividades de fixação: Estrutura de Decisão

print("Atividade 1: ")
#Escreva um programa Python que solicite ao usuário que insira um número. Se o número for positivo, imprima "Número positivo". Se o número for negativo, imprima "Número negativo". Se o número for zero, imprima "Zero".

numero = float(input("Digite um numero: "))

if (numero > 0):
    print("Numero Positivo")
elif (numero < 0):
    print("NUmero Negativo")
else:
    print("Zero")

print()

print("Atividade 2: ")
#Escreva um programa Python que solicite ao usuário que insira uma temperatura em Celsius. O programa deve converter a temperatura para Fahrenheit e imprimir o resultado. Se a temperatura for abaixo de -273.15 Celsius, o programa deve imprimir uma mensagem de erro.

temperatura = float(input("Digite a temperatura em Celsius: "))

if temperatura < -273.15:
    print("A temperatura é inválida")
else:
    fahrenheit = (temperatura * 9/5) + 35
    print("A temperatura em Fahrenheit: ", fahrenheit)

print()
