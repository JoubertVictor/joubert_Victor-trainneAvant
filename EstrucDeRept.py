#Exercicios de Estrutura de Repetições:

print("Atividade 1: ")
#1. **Fácil**:
# ..a)Escreva um programa para encontrar a soma S = 3 + 6 + 9 + …. + 333.
# ..b)Escreva um programa que leia 10 notas e informe a média dos alunos.
# ..c) Escreva um programa que leia um número de 1 a 10, e mostre a tabuada desse número

print("a)")
soma = 0

for numero in range(3, 333, 3):
    soma = soma + numero

print("Somatoria de S é: ", soma)

print("\nb)")

total_notas = 0
for notas in range(1, 11):
    nota = float(input("Digite a nota: "))
    total_notas = total_notas + nota

media_notas = total_notas/10
print(f"A média das notas é: {media_notas:.2f}")

print("\nc)")
tabuada = int(input("Tabuada de 1 a 10: "))

for i in range(1, 11):
    produto = tabuada * i
    print(f"{tabuada} x {i} = {produto}")

print("\nAtvidade 2: ")
#Fácil: Escreva um programa que imprima na tela os números de 1 a 10 usando um laço for.

for i in range(1, 11):
    print(i)

print("\nAtvidade 3: ")
#Médio: Escreva um programa que solicite ao usuário que insira 5 números e, em seguida, imprima a soma desses números utilizando um laço while.

soma = 0
count = 0

while count < 5 :
    num = float(input("Digite os numeros: "))
    soma = soma + num
    count = count + 1

print(f"A soma dos numeros é: {soma}")

print("\nAtvidade 4: ")
#Difícil: Escreva um programa que imprima todos os números pares entre 1 e 100 utilizando um laço for.


for i in range(1, 101):
    if i % 2 == 0:
        print(i)

print("\nAtvidade 5: ")
#Muito difícil: Escreva um programa que solicite ao usuário que insira um número inteiro, e então imprima a tabuada desse número utilizando um laço for.

a = int(input("Digite um número: "))
for i in range(1, 11):
    print(a, "x", i, "=", a * i)
