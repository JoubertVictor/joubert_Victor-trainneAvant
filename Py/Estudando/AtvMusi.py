class Musico:
    def __init__(self, nome):
        self.nome = nome
    
    def tocar_instrumento(self):
        pass

class Percursor(Musico):
    def tocar_instrumento(self):
        print(f"{self.nome} sou o percursonista!!!")
        
class Pianista(Musico):
    def tocar_instrumento(self):
        print(f"{self.nome} sou o pianista!!!")
        
def main():
    percu = Percursor("Jose")
    piani = Pianista("Pedro")
    
    percu.tocar_instrumento()
    piani.tocar_instrumento()

main()
