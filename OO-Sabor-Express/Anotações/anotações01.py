
# O que é uma classe?
#Resposta: Uma classe caracteriza um tipo especifico de objeto. Por exemplo

#   class Carro: --> Isso é uma classe que vai caracteriza4r o objeto Carro
#       def __init__(self, marca, modelo, cor) --> Isso é um método especial da classe, chamado de construtor, ele  inicializa os atributos do objeto com os valores fornecidos
    #       self.cor = vermelho --> Artibutos da classe
    #       self.modelo = Sedan --> Artibutos da classe
    #       Self.marca = Toyota --> Artibutos da classe

#       def acelerar (self): --> É uma função que quando chamada  ira imprimir essa mensagem
#           print(f' O {self.marca} { self.modelo} está acelerando)

#       def frear(self): --> É uma função que quando chamada  ira imprimir essa mensagem
#           print(f'O {self.marca} { self.modelo} está freando )

#o que são objetos?
#Resposta: É uma instancia da classe, é quando criamos uma variavel para armazenar os dados e quando chamamamos a classe, atribuimos valores a ela. 
# Por exemplo:

#carro1 = Carro('Toyta', 'Corola', ' Vermelho')
#carro2 = Carro('Nissan', 'Corola', ' Azul')

#print(carr01) --> Saida do Toyota
#print(carr02) --> Saida do Nissan

#carro01.acelerar() --> Chamada da função que vai indicar que o carro01 Toyota esta acelerando
#carro02.desacelerando() --> Chamada da função que vai indicar que o carro01 Toyota esta desacelerando