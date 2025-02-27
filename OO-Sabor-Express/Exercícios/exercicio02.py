#Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. 
#Crie uma instância dessa classe e atribua valores aos seus atributos.

class carro:
    modelo = ''
    cor = ''
    ano = ''

my_car = carro()
my_car.modelo = "Ford"
my_car.cor = 'Dark'
my_car.ano = '2025'

print(vars(my_car))

#Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. 
#Instancie um restaurante e atribua valores aos seus atributos.
class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

restaurantes = Restaurante('Costela no Bafo', 'Churascarria')
print(vars(restaurantes))
