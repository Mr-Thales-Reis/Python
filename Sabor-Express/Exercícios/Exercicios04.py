dados_de_usuarios = {'nome': 'João', 'idade':'20', 'cidade': 'Pouso Alegre'}
print(dados_de_usuarios)

dados_de_usuarios['idade'] = 40
print(dados_de_usuarios)

dados_de_usuarios['Profissão'] = 'Software enginear'
print(dados_de_usuarios)

del dados_de_usuarios['cidade']
print(dados_de_usuarios)

Quadrado = { 1:1, 2:4, 3:9, 4:16, 5:25}
print(Quadrado)

logico = { "Chave01" : 10, 'Chave02' : 20}
chave = 'Chave02'
if chave in  logico:
    print(f'A chave {chave} existe no dicionario')
else:
    print(f'A chave {chave} não existe no dicionario')

