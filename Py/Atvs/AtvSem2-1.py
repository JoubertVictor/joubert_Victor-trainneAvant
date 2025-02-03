class Hotel:
    def __init__(self, nome_hotel):
        self.nome_hotel = nome_hotel
   
    def determineContaCliente(self, cliente):
        return cliente.fornecaValorConta()

class Cliente:    
    def __init__(self, nome, dias_estadia, consumo_restaurante):
        try:
            if not isinstance(nome, str):
                raise ValueError(f"Erro: o nome deve ser uma string.")
            
            if not isinstance(dias_estadia, int) or dias_estadia < 0:
                raise ValueError(f"Erro: dias de estadia devem ser um número inteiro não negativo.")
            
            if not isinstance(consumo_restaurante, int) or consumo_restaurante < 0:
                raise ValueError(f"Erro: consumo no restaurante deve ser um número inteiro não negativo.")

            self.nome = nome
            self.dias_estadia = dias_estadia
            self.consumo_restaurante = consumo_restaurante
        
        except ValueError as e:
            print(e)
            self.nome = None
            self.dias_estadia = None
            self.consumo_restaurante = None
    
    def fornecaValorConta(self):
        if self.nome is not None:
            return 100 * self.dias_estadia + self.consumo_restaurante * 50
        else:
            return 0
    
def main():
    cliente = Cliente("Bernado Betoneira", 10, 21)
    hotel = Hotel("Hotel Perna de Pau, Cabeça de Elefante")

    valor_conta = hotel.determineContaCliente(cliente)  
    
    if cliente.nome is not None:
        print()
        print(f"O cliente {cliente.nome} que ficou {cliente.dias_estadia} dias no {hotel.nome_hotel} "
              f"teve a conta de R${valor_conta} reais, considerando {cliente.dias_estadia} dias de hospedagem "
              f"e {cliente.consumo_restaurante} refeições.")
    else:
        print("Erro ao criar o cliente devido a valores inválidos.")
        
main()