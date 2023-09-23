# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# # Exemplo 01
# for numero in [0,18,56,77,95]:
#     print(f'Número: {numero}. ')
# else:
#     print('Acabou')
#
# # Exemplo 02
# for numero in range (100000):
#     print(numero)
#     if numero == 4:
#         break
# print ('Até mais.')
#
# # Exemplo 03
# for x in [1,10,20,30,40,50]:
#     if x == 30:
#         continue
# print(f'O número é {x}')
#
#-------------------------------------------------------------------------------------------------------------
# # Exercício 01
# soma = 0
# quantidade = 20
#
# for i in range (quantidade):
#     valor = float(input(f'Digite o {i+1}º valor: '))
#     soma+=valor
#
# media = soma/quantidade
#
# print(f'Soma dos valores: {soma}')
# print(f'Media dos valores: {media}')
#
# # Exercício 02
# for i in range (2,100,2):
#     print(i)
#
# # Exercício 03
# for i in range (1,100,2):
#     print(i)
#
# # Exercicio 04
#
# soma = 0
# for i in range (2,100,2):
#     soma+=1
# print(f'A soma dos números pares é: {soma}')

# Exercício 05

# soma = 0
# for i in range (2,100,2):
#     soma+=1
# print(f'A soma dos números pares é: {soma}')

# for i in range (10):
#    idade = int(input(f'Digite a idade da {i+1}º pessoa: '))
#   if 5 <= idade <= 7:
#       print(f'A {i+1} pessoa vai para a categoria Infantil A')
#   elif 8 <= idade <= 11:
#       print(f'A {i+1} pessoa vai para a categoria Infantil B')
#   elif 12 <= idade <= 12:
#    print(f'A {i+1} pessoa vai para a categoria Juvenil')
#   else:
#       categoria = 'Outra categoria'
#   print(f'A {i+1} pessoa vai para a Outra Categoria')


#-------------------------------------------------------------------------------------------------------------


# Exercícios usando o WHILE


# Exercício 01
# soma = 0
# numero = None
#
# while numero != 0:
#     numero = int(input('Digite um número intero, ou 0 para sair: '))
#     soma += numero
#
# print(f'A soma dos números informados é {soma}.')

# Exercicio 02
#
# maior = None
#
# while True:
#     numero = int(input('Digite um número intero, ou 0 para sair: '))
#     if numero == 0:
#         break
#
#     elif maior is None or numero > maior:
#         maior = numero
#
#     elif maior is not None:
#         print(f'O maior valor digitado foi {maior}')
#     else:
#         print('Nenhum valor foi digitado.')


# Exercício 03
#
# soma = 0
# contador = 0
#
#
# while numero !=0:
#     numero = int(input('Digite um número inteiro, ou 0 para sair: '))
#     if numero == 0:
#         break
#
#     soma += numero
#     contador +=1
#
#     if contador == 0:
#         print('Nenhum número foi digitado.')
#     else:
#         media = soma / contador
#         print(f'Soma dos valores: {soma}')
#         print(f'Média dos valores digitados {media}')
#
# # Exercício 04
#
# soma = 0
# numero = None
#
# while numero != 0:
#     numero = int(input('Digite um número inteiro, ou 0 para sair: '))
#     if numero == 0:
#         break
#
#     if numero % 2 == 0:
#         soma+=numero
#
#     print(f'A soma dos valores pares é {soma}')

# Exercício 05

# idades = []
#
# while True:
#     idade = int(input('Digite a idade (Ou um numero negativo para parar)'))
#
#     if idade<0:
#         break
#
#
#     idades.append(idade)
#
#     if not idades:
#         print('Nenhuma idade foi inserida')
#     else:
#         maior = max(idades)
#         menor = min(idades)
#         soma = sum(idades)
#         media = soma // len(idades)
#
#         print(f'Maior idade: {maior}')
#         print(f'Menor idade: {menor}')
#         print(f'Soma das idades {soma}: ')
#         print(f'Média das idades {media}: ')





# Exercicio 06
#
# numero = int(input('Digite o número para o qual deseja calcular a tabuada: '))
# contador = 1
#
# while contador <= 10:
#     resultado = numero * contador
#     print(f'{numero} x {contador} = {resultado}')
#     contador+=1


# FUNÇÕES

# def soma():
#     r = 2 + 2
#     print (r)
#
#     --------------------------------

def Soma(x,y):
    print(x +y)

def Sub(x,y):
    print(x-y)

def mult(x,y):
    print(x*y)

def dividir(x,y):
    print(x/y)












