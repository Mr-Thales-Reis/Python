



#Crie uma classe chamada Veiculo com um método abstrato chamado ligar.

#No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.

#Crie uma nova classe chamada Carro que herda da classe Veiculo.

#No construtor da classe Carro, 
#utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.

#Em um arquivo chamado main.py, importe a classe Carro.

#No arquivo main.py, instancie três objetos da classe Carro com diferentes características, como marca, modelo e cor.

from abc import ABC, abstractmethod #-> importando o módulo abc para criar a classe abstrata

class Veiculo(ABC): # -> dizendo que a classe veiculo é uma classe abstrata
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    @abstractmethod # -> Método abstrato que deve ser implementado por todas as subclasses de 'Veiculo'
    def ligar(self):
        pass

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor
    
    # Implementação do método abstrato 'ligar' na subclasse 'Carro'
    def ligar(self):
        # Exibe uma mensagem indicando que o carro está ligado
        print(f"O {self.marca} {self.modelo} de cor {self.cor} está ligado.")
