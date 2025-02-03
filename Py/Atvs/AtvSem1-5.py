class FazBolo:
    def __init__(self, massa, recheio, cobertura, temperatura):
        self.massa = massa
        self.recheio = recheio
        self.cobertura = cobertura
        self.temperatura = temperatura

    def assar(self):
        temponoforno = 0

        #Restringindo a numeros positivos
        try:
            tempo = int(input("Insira o tempo em minutos para assar o bolo: "))
            if tempo < 0 :
                raise ValueError("O tempo não pode ser negativo.")
            
            if self.temperatura not in ["alto", "médio", "baixo"]:
                raise ValueError("Temperatura inválida! Use 'alto', 'médio' ou 'baixo'.")
            
            #Começando 
            if self.temperatura == "alto":
                tempo_assar = 10
                print(f"Você está querendo assar o bolo no fogo ALTO por {tempo} minutos.")
                if tempo < tempo_assar:
                    print("O bolo ficará cru.")
                elif tempo > tempo_assar:
                    print("Cuidado! O bolo pode queimar.")
                else:
                    print("O bolo está perfeitamente assado!")
            
            elif self.temperatura == "médio":
                tempo_assar = 30
                print(f"Você está querendo assar o bolo no fogo MÉDIO por {tempo} minutos.")
                if tempo < tempo_assar:
                    print("O bolo ficará cru.")
                elif tempo > tempo_assar:
                    print("Cuidado! O bolo pode queimar.")
                else:
                    print("O bolo está perfeitamente assado!")
            
            elif self.temperatura == "baixo":
                tempo_assar = 45
                print(f"Você está querendo assar o bolo no fogo BAIXO por {tempo} minutos.")
                if tempo < tempo_assar:
                    print("O bolo ficará cru.")
                elif tempo > tempo_assar:
                    print("Cuidado! O bolo pode queimar.")
                else:
                    print("O bolo está perfeitamente assado!")

        except ValueError as ve:
            print(f"Erro: {ve}")

bolo = FazBolo(500, "Chocolate", True, "médio")
bolo.assar()
