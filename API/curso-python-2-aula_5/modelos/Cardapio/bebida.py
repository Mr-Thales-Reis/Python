from modelos.Cardapio.item_cardapio import item_cardapio

class Bebida(item_cardapio):
    def __init__(self, nome, preco, tamanho):
       super().__init__(nome, preco) # Isso é uma herança
       self.tamanho = tamanho