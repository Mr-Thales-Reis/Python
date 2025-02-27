#Claase abstrata -> É a classe que diz o que se deve fazer no código

#SubClasse -> É a classe que recebe os padrões da Classe Abstrata e realiza a ação

#Exemplo
from abc import ABC, abstractmethod

# Classe abstrata (plano)
class Veiculo(ABC):
    @abstractmethod
    def ligar(self):
        pass  # Apenas uma instrução, sem detalhes

# Classe que completa o plano
class Carro(Veiculo):
    def ligar(self):
        print("Carro ligado!")  # Detalhes específicos do carro

# Usando a classe concreta
meu_carro = Carro()
meu_carro.ligar()  # Vai mostrar "Carro ligado!"