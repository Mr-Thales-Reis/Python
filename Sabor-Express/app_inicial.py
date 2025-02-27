import os
# Isso é um dicionário dentro de uma lista
#                  Chave:valor
restaurantes = [ {'nome':'Praça', 'categoria':'Japonesa', 'ativo': False},
                {'nome': 'Pizza SUprema', 'categoria': 'Pizza', 'ativo': True},
                {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}]

#Essa função retorna o nome do programa
def nomePrograma():
    print('𝔖𝔞𝔟𝔬𝔯 𝔈𝔵𝔭𝔯𝔢𝔰\n')

#Essa função retorna as opções possíveis para a escolha do usuário
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Altenar estado do restaurante')
    print('4. Sai\n')

#Essa função retorna uma ação de finalização do programa e exibe uma mensagem garantindo a finalização
def finlizar_app():
    exibir_subtitulo('Finalizar programa')

def voltar_ao_menu_principal():
    input('Digite uma tecla para voltar ao menu ')
    main()

#Caso o usuário escolha uma opção inválida essa função além de exibir uma mensagem dizendo que a opção é invalidada ainda faz voltar ao menu principal
def opcao_invalida():
    print("Essa opção é invalida!\n")

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


#Essa função possibilita o cadastramento de novos restaurantes
def cadastrar_novo_restaurante():
    exibir_subtitulo('cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria =  input(f'Digite o nome da caegoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante =  { 'nome': nome_do_restaurante, 'categoria':categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadstrado com sucesso!')
    voltar_ao_menu_principal()

#Essa função usa do laço de repetição FOR para mostrar os restaurantes listados na lista( restaurantes = [])
def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} | {'categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternar estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes: 
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    # O python vai tentar rodar esse código
    try:
    #Quando vamos utilizar condicionais temos que informar qual o tipo de variável
        opcaoEscolhida = int(input('Escolha uma opção: '))
        if opcaoEscolhida == 1:
          print('Cadastrar restaurante')
          cadastrar_novo_restaurante()
        elif opcaoEscolhida == 2:
           print('Listar restaurante')
           listar_restaurantes()
        elif opcaoEscolhida == 3:
           alternar_estado_restaurante()
        elif opcaoEscolhida == 4:
           finlizar_app()
        else:
            opcao_invalida()
    #Se ele não conseguir vai ativar essa função que criamos. Por exemplo: Try(Tente) Se não der certo(except)
    except:
        opcao_invalida()

#Aqui é onde todas as funções criadas estão alocadas
def main():
    os.system('cls')
    nomePrograma()
    exibir_opcoes()
    escolher_opcao()

# Dessa forma eu falo para o Python que o MAIN será o meu códiogo/programa principal
if __name__  == '__main__':
    main()
