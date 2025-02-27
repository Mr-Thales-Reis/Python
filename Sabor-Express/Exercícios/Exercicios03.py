#1 - Crie uma lista para cada informação a seguir:
#Lista de números de 1 a 10;
#Lista com quatro nomes;
#Lista com o ano que você nasceu e o ano atual.

numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros)

nomes = ['Thales', 'Marcelo', 'João', 'Miguel']
print(nomes)

data = ['Data de nascimento: 2003', 'Ano atual: 2024']
print(data)

#Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
num = [1,2,3,4,5,6,7,8,9,10]
for i in num:
    print(i)

# Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
soma = 0
for numero in range(1,11): # RANGE() cria uma sequência de números 
    if numero % 2 != 0:
        soma+= numero # soma inicializa com 0, ai pra cada cada vez que se repassa o laço ela faz outra soma com o valor anterior 
    
print("A soma dos números ímpares de 1 a 10 é:", soma)

#Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
for a in range(10, 0, -1):
    print(a)

#Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
n1 = int(input('Digite um número: '))
for tabuada in range(1,11):
    soma = n1 * tabuada
    print(f'{n1} X {tabuada} = {soma}')