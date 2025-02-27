class Restaurante:
    #Essa lista é um atributo da clase restaurante. Todos os objetos criados desta classe são armazenados na lista
    restaurantes = []

    def __init__(self, nome, categoria):
        #TITLE() deixa a letra inicial com letra maiuscula
        self._nome = nome.title()
        # .upper() deixa todas as letras em maiusculas
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

#Faz uma modificação de como um atributo é lido
#Aui no caso o propety esta retornando esse comando lógico
    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('pizza express', 'Italiana')

Restaurante.listar_restaurantes()
