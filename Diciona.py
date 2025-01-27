#Exercico de fixação Dicionários


print("Atividade 1: ")
#Fácil: Crie um dicionário com 5 nomes de cidades como chaves e suas populações como valores. Em seguida, imprima a população de uma das cidades.


cidades = {
    'Natal': 320548,
    'Belo Horizonte': 2032001,
    'Pompeu':  31812 ,
    'Curitiba': 1250122,
    'Porto Alegre': 1333212
}


print(cidades['Natal'])


print("\nAtividade 2: ")
#Médio: Adicione um novo par chave-valor ao dicionário do exercício anterior representando outra cidade e sua população. Em seguida, imprima o dicionário atualizado


cidades['Niteroi'] =  487327
print(cidades)


print("\nAtividade 3: ")
#Difícil: Remova um par chave-valor do dicionário do exercício anterior. Em seguida, imprima o dicionário atualizado.


del cidades['Curitiba']
print(cidades)

