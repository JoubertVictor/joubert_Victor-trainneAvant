#Exerciciso de fixação, Bibliotecas

#impotando todas as bibliotecas necessarias


print("Atividade 1: ")
#Fácil: Use a biblioteca math para calcular a raiz quadrada de um número. Para esse exercício, o número pode ser qualquer um que você escolher.

import math

numero = int(input("Digite um numero inteiro: "))
raiz_quadradada = math.sqrt(numero)
print(raiz_quadradada)

print("\nAtividade 2: ")
#Médio: Use a biblioteca random para gerar um número aleatório entre 1 e 10. Em seguida, peça ao usuário para adivinhar esse número. Se o usuário adivinhar corretamente, imprima "Parabéns! Você adivinhou corretamente!". Caso contrário, imprima "Desculpe, tente novamente.".

import random

numero_aleatorio = random.randint(1,10)
advinhar = int(input("Adivinhe o numero de 1 a 10: "))

if advinhar == numero_aleatorio:
    print("Parabéns! Você adivinhou corretamente!")
else:
    print("Desculpe, tente novamente")

print("\nAtividade 3: ")
#Médio-Alto: Use as bibliotecas os e datetime para criar um script que imprime o diretório atual e a data e hora atuais.

import os
import datetime

diretorio_atual = os.getcwd()
data_hora_atuais = datetime.datetime.now()

print("Voce esta no diretório: ", diretorio_atual)
print("Data e Hora atuais: ", data_hora_atuais)
