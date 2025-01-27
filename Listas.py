#Atividades de fixação: Listas

print("Atividade 1: ")
#Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# a) tamanho da lista.
# b) maior valor da lista.
# c) menor valor da lista.
# d) soma de todos os elementos da lista.
# e) lista em ordem crescente.
# f) lista em ordem decrescente.

L = [5, 7, 2, 9, 4, 1, 3]

print("a) Tamanho da lista: ", len(L))

print("b) Maior valor da lista: ", max(L))

print("c) Menor valor da lista: ", min(L))

print("d) Soma de todos os elementos da lista: ", sum(L))

L.sort()
print("e) Lista em ordem crescente: ", L)

L.reverse()
print("f) Lista em ordem decrescente: ", L)

print()

print("Atividade 2: ")
#   a) Adicione um novo elemento ao final da lista criada no exercício anterior e imprima novamente a lista.
#   b) Crie uma lista com 5 elementos (pode ser de qualquer tipo). Em seguida, imprima a lista.
#   c) Crie uma lista com números de 1 a 10 e imprima todos os números pares da lista.

L.append(21)
print(L)

print("a)")
Aleatorio = ['Batata', 2019, 'Alex', 2589, 'Guilherme']
print(Aleatorio)
print()

print("b)")
numero_par = list(range(0, 10, 2))
print(numero_par)
print()


print("Atividade 3: ")
# a) Crie duas listas, uma com números de 1 a 5 e outra com números de 6 a 10. Concatene as duas listas e imprima o resultado.
# b) Crie uma lista com números de 1 a 10. Use slicing (fatiamento) para imprimir apenas os números de 5 a 8.
# c) Crie uma lista com os números pares de 2 a 20 utilizando a função range(). Imprima a lista.

print("a)")
Lista1 = list(range(1,6))
Lista2 = list(range(6,11))

Lista = Lista1 + Lista2

print(Lista)
print()

print("b)")
Lista_numeros = list(range(1,11))
print(Lista_numeros[4:8])
print()

print("c) ")
Lista_pares = list(range(2,21,2))
print(Lista_pares)
print()