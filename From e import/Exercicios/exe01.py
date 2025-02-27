#   Crie uma Classe Pai (Veiculo): Implemente uma classe chamada Veiculo com um construtor que aceita dois parâmetros, marca e modelo. 
# A classe deve ter um atributo protegido _ligado inicializado como False por padrão.

#   Construa o Método Especial str: Adicione um método especial str à classe Veiculo que 
#retorna uma mensagem formatada com a marca, modelo e o estado de ligado/desligado do veículo.

#Crie uma Classe Filha (Carro): Agora, crie uma classe chamada Carro que herda da classe Veiculo. 
#No construtor da classe Carro, inclua um novo atributo chamado portas que indica a quantidade de portas do carro.

#Implemente o Método Especial str na Classe Filha: Adicione um método especial str à classe Carro 
#que estenda o método da classe pai (Veiculo) e inclua a informação sobre a quantidade de portas do carro.

#Crie uma Classe Filha (Moto): Similarmente, crie uma classe chamada Moto que também herda de Veiculo. 
#Adicione um novo atributo chamado tipo ao construtor, indicando se a moto é esportiva ou casual.

#Classe PAI
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        estado = 'Ligado' if self._ligado else 'Desligado'
        return f'{self.marca} | {self.modelo} | {estado}'
    

# Classe Filha
class Carro(Veiculo):
    def __init__(self, marca, modelo, portas): # Esses são os atibutos da classe filha(Carro)
        super().__init__(marca, modelo)  # Chama o construtor da classe pai (Veiculo)
        self.portas = portas
    
    def __str__(self):
        descricao_veiculo = super().__str__() # -> Chama o método __str__ da classe pai
        return f'{descricao_veiculo} | {self.portas}'# -> Adiciona a informação sobre as portas

# Classe Filha (Moto)
class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo
    
    def __str__(self):
        descricao_veiculo = super().__str__()
        return f'{descricao_veiculo} | Tipo: {self.tipo}'
    

