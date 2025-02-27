#Aqui vamos imprtar  do restaurante-Alura a classe restaurante
from modeloae.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_mexicana = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa',"Japonesa")

def main():
    Restaurante.listar_restaurantes()
    
if __name__ == '__main__':
    main()