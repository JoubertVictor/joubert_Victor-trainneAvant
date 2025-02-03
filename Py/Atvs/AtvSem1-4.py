class Bolo:
    def __init__(self, nome, recheio, massa, cobertura):
        self.nome = nome
        self.recheio = recheio
        self.massa = massa
        self.cobertura = cobertura

Bolo1 = Bolo("Bolo Fofo", "Prestigio", 400, True)
Bolo2 = Bolo("Bolo Supreme", "Brigadeiro", 500, False)

print()
print("Advindo da instância principal ")
print()
Bolo3 = Bolo("Bolo Fofo", "Prestigio", 400, False)

print(Bolo1.cobertura)
print(Bolo2.cobertura)
print(Bolo3.cobertura)

print()
print("Advindo do primeiro bolo")
print()

Bolo3b = Bolo1
Bolo3b.cobertura = False

print(Bolo1.cobertura)
print(Bolo2.cobertura)
print(Bolo3b.cobertura)

print()