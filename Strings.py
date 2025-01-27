#Exercicios de Fixação -- Strings

print("Atividade 1: ")
#Considere a string A= “Drone bom é drone voando”. Que fatia corresponde a “drone voando”?

A = "Drone bom é drone voando"

print(len(A))

print(A[12:])
print("Corresponde a A[12:]\n")

print("Atividade 2: ")
#Escreva um programa que solicite uma frase ao usuário e escreva a frase toda em maiúscula e sem espaços em branco.

frase = input("")
#frase_minuscula = frase.upper()
frase_final = frase.replace(" ", "").upper()
print(frase_final)
print()

print("Atividade 3: ")
#Escreva um programa que solicite ao usuário que insira uma palavra e, em seguida, imprima o inverso dessa palavra.

palavra = input("Digite uma palavra: ")
print(palavra)

palavra_invertida = palavra[::-1]

print(palavra_invertida)