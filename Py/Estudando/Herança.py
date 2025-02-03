# Classe principal
class Animal:
    def fazer_som(self):
        """Método genérico que deve ser implementado pelas subclasses."""
        print("Som genérico de animal")

# Subclasse Cachorro que herda de Animal
class Cachorro(Animal):
    def fazer_som(self):
        """Método que sobrescreve fazer_som para imprimir o som de um cachorro."""
        print("AUAU")

# Testando as classes
if __name__ == "__main__":
    # Criamos um objeto da classe Cachorro
    meu_cachorro = Cachorro()
    
    # Chamamos o método fazer_som
    meu_cachorro.fazer_som()
