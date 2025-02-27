#Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. 
#Inicie o atributo ativo como False por padrão.
class ContaBancaria:
#                                     --> Esse método armazena as informações da classe!
    def __init__(self, titular, saldo):
        self.titular =titular
        self.saldo = saldo
        self.ativo = False
#                     --> Esse método armazena as informações do init e gera uma mensagem com ela!
    def __str__(self):
        return f'O senhor {self.titular}, possui em conta o valor de R$ {self.saldo}'

#
    def ativar_conta(self):
        self.ativo = not self.ativo

#Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. 
#Crie duas instâncias da classe e imprima essas instâncias.

Status = ContaBancaria("Thales Reis", 5500)
print(Status)

#Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. 
#Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
Status.ativar_conta()
print(f'O Status da conta é {Status.ativo}')

#Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário