class Carro:
    def __init__(self, modelo, cor):
        if not isinstance(modelo, str):
            raise TypeError("Modelo em formato incorreto")
        
        if not isinstance(cor, str):
            raise TypeError("Cor em formato incorreto")
        
        self.modelo = modelo
        self.cor = cor
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        self.ligado = True
        print("Ligando o carro")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0
            print("Desligando carro")
        else:
            print("Carro já está desligado")

    def acelerar(self, velocidade):
        if self.ligado:
            if 0 <= velocidade <= 200:
                self.velocidade = velocidade
                print(f"Acelerando para {self.velocidade} km/h")
            else:
                print("O carro já está em sua velocidade máxima: 200 km/h")
        else:
            print("O carro está desligado, ligue para acelerar")

class Motorista:
    def __init__(self, nome_motorista):
        if not isinstance(nome_motorista, str):
            raise TypeError("Nome do motorista em formato inválido")
        self.nome_motorista = nome_motorista

    def dirigir(self, carro, velocidade):
        print()
        print(f"{self.nome_motorista} está dirigindo o {carro.modelo} da cor {carro.cor}.")
        carro.ligar()
        carro.acelerar(velocidade)

def main():
    op = int(input("Digite 0 para criar seu carro ou 1 so pra ver o codigo funcionando: "))
    if op == 1:
        carro1 = Carro("Gt", "Laranja")
        carro2 = Carro("Mustang", "Azul")
        carro3 = Carro("Uno Fiat", "Prata")

        motorista1 = Motorista("Afonso")
        motorista2 = Motorista("Mirela")
        motorista3 = Motorista("Pereira")

        motorista1.dirigir(carro1, 64)
        motorista2.dirigir(carro2, 185)
        motorista3.dirigir(carro3, 71)

        print()
        print("Testando desligar o carro e acelerar qnd desligado:")
        carro1.desligar()
        carro1.acelerar(150)
    elif op == 0:
        modelo = input("Digite o modelo do carro: ")
        print()
        cor = input("Digite a cor do carro: ")
        print()
        carro = Carro(modelo, cor)
        nome_motorista = input("Digite o nome do motorista: ")
        print()
        motorista = Motorista(nome_motorista)
        velocidade = int(input("Digite a velocidade para acelerar: "))
        print()
        motorista.dirigir(carro, velocidade)
    else:
        print("Digitou algo diferente de 0 ou 1")

main()