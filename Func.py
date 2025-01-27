#Atividade de Funções:

print("Atividade 1: ")
#Crie uma função para desenhar uma linha, usando o caractere '_'. O tamanho da linha deve ser definido na chamada da função.  

def desenhar_linha(tamanho):
    print('_' * tamanho)

tamanho = int(input("Digite o tamanho da linha: "))
desenhar_linha(tamanho)


print("\nAtividade 2: ")
#Crie uma função que receba como parâmetro uma lista, com valores de qualquer tipo. A função deve imprimir todos os elementos da lista numerando-os.

def elementos(lista):

    for i in range(len(lista)):
        print(f"{i + 1}. {lista[i]}")

minha_lista = ['Avant', 'Pitanga', 874, 56, [54, 68, 1, 96, 10], ['eu', 'vc', 'batata'], [1, 2, 3]]
elementos(minha_lista)


print("\nAtividade 3: ")
#Crie uma função que receba como parâmetro uma lista com valores numéricos e retorne a média desses valores.

def calculando_media(lista1):
    
    soma = sum(lista1)
    media = soma / len(lista1)
    return media

minha_lista1 = [10, 10, 25, 24, 70, 62, 17]
media = calculando_media(minha_lista1)
print(f"A média dos valores é: {media}")


print("\nAtividade 4: ")
#(Nível Médio) Crie uma função que receba uma lista de números e retorne o maior e o menor número da lista. A função deve retornar ambos os números na forma de uma tupla.

def maior_menor(lista2):

    maior_numero = max(lista2)
    menor_numero = min(lista2)
    
    return (maior_numero, menor_numero)

minha_lista2 = [25, 5, 20, 3, 8]
resultado = maior_menor(minha_lista2)
print(f"A tupla com o maior e o menor número é: {resultado}")

print("\nAtividade 5: ")
#(Nível Médio) Crie uma função que receba um número inteiro e retorne uma lista com todos os seus divisores.

def divisores(numero):

    lista_divisores = []

    for i in range(1, numero + 1):
        if numero % i == 0:
            lista_divisores.append(i)
    return lista_divisores

numero = int(input("Digite um número inteiro: "))
resultado = divisores(numero)
print(f"Os divisores de {numero} são: {resultado}")
