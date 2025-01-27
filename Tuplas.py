#Fixação de Tuplas

# ..Nível Fácil:
# 1. Crie uma tupla com quatro elementos de diferentes tipos e imprima cada um deles.
# 2. Crie duas tuplas e concatene-as em uma terceira tupla. Imprima a nova tupla.
# 3. Crie uma tupla com números de 1 a 10 e use a função `len()` para imprimir a quantidade de elementos na tupla.

# ..Nível Médio:
# 1. Crie uma tupla com números de 1 a 10 e use a função `max()` e `min()` para encontrar o valor máximo e mínimo.
# 2. Crie uma tupla de tuplas, também conhecida como tupla aninhada, e imprima o segundo elemento da segunda tupla.
# 3. Crie uma tupla com números e escreva um programa para ordenar a tupla em ordem crescente.

print("Nível Fácil: \n")
print("1. \n")

T = ('Richarlison', 24, 'Uva', 72)
print(T)
print()

print("2.\n")
Tupla1 = ('Vermelho', 'Purpura', 'Reno', 144)
Tupla2 = (154, 'Pereira', 'Pedestre', 988)
Tupla3 = Tupla1 + Tupla2
print(Tupla3)
print()

print("3.\n")
Tupla_1a10 = (1,2,3,4,5,6,7,8,9,10)
print("Tamanho da tupla: ", len(Tupla_1a10))
print()

print("Nível Médio: \n")
print("1.\n")

Tupla_Numeros = tuple(range(1,10))
print("Máximo: ", max(Tupla_Numeros))
print("Mínimo: ", min(Tupla_Numeros))
print()

print("2.\n")
tupla_aninhada = (('Abacate', 3, 'Preto'), ('Amora', 98, 'Zika'), (89, 'Moto', 125))
print("Segundo elemento da segunda tupla:", tupla_aninhada[1][1])
print()

print("3.\n")
tupla_desordenada = (5,69,7,54,78,36,54,12,85,33)
tupla_ordenada = tuple(sorted(tupla_desordenada))
print("Tupla ordenada em ordem crescente: ", tupla_ordenada)
print()