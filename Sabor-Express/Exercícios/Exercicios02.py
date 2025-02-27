senhaCadastrado = input('Digite sua senha:')
nomeCadastrado = input('Qual seu nome:')

senhaUsuario = input('Digite sua senha:')
nomeUsuario = input('Digíte seu nome: ')

if senhaCadastrado == senhaUsuario and nomeCadastrado == nomeUsuario:
    print('Acesso liberado ')
else:
    print('Acesso negado ')


x = int(input('X = '))
y = int(input('Y = '))

if x > 0 and y > 0:
    print('Primeiro quadrante')
elif x < 0 and y > 0:
    print('Segundo quadrante')
elif x < 0 and y < 0:
    print('Terceiro quadrante')
elif x > 0 and y < 0:
    print("Quarto quadrante")
else:
    print('O ponto esta no eixo ou origem')