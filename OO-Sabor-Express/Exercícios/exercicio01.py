class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praça = Restaurante()
restaurante_praça.nome = 'Praça'
restaurante_praça.categoria = 'Italiana'
restaurante_praça.ativo = False

print("Restaurante Praça")
print(vars(restaurante_praça))


if restaurante_praça.ativo == True:
    print("o Restaurnte está ativo")
else:
    print("O restaurante não esta ativo")

restaurante_praça.nome = 'Bistrô'
print(vars(restaurante_praça))

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
restaurante_pizza.ativo = True
print("Restaurante Pizza Place")
print(vars(restaurante_pizza))

if restaurante_pizza.categoria == 'Fast Food':
    print('Sim está certo')
else:
    print("Não está certo")

print((restaurante_pizza.nome, restaurante_pizza.categoria))

