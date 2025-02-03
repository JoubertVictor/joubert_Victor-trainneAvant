class Automovel:
    def motor(self):
        print("Motor padrão")
        
class Moto(Automovel):
    def motor(self):
        return "V8"

def main():
    motors= Moto()
    print(motors.motor())
    
main()