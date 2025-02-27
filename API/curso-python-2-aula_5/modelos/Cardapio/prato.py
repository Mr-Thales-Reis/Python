from modelos.Cardapio.item_cardapio import item_cardapio #-> Aqui eu etou importando a classe Item_cardapio, ou seja agora ela é minha classe pai
class prato(item_cardapio):
    def __init__(self, nome, preco, descricao): #-> Isso aqui é um método construtor, ele é responsavel por receber os valores do objeto
        super().__init__(nome, preco)           # -> Aqui eu estou pegando atributos da classe PAI        
        self.descricao = descricao                                                                                                