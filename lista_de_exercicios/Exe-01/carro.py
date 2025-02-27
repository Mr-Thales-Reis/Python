from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
         super().__init__(marca, modelo)
         self.portas = portas
    
    def __str__(self):
         return super().__str__() + f"Tem {self.portas} portas"  # Dessa forma eu adiciono uma String a classe pai