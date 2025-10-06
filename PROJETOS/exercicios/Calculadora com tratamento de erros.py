# Carlos está criando uma calculadora simples, mas quer garantir que o programa não quebre se o usuário digitar valores inválidos, ele precisa tratar os erros.

# Crie uma calculadora que permita ao usuário escolher entre soma, subtração, multiplicação e divisão. Além de modularizar o código em funções, use try-except para tratar erros de entrada inválida, que consiste em:

# Caso digite um caractere em vez de número | exceção a ser lançada: ValueError;
# Caso tente fazer uma divisão por 0 | exceção a ser lançada: ZeroDivisionError.

'''SOLUCAO RONDINELLE'''
import os
os.system('cls')

def somar(a,b):
    soma = a + b
    print(f'Resultado: {soma:.2f}') 

def subtratir(a,b):
    subtracao = a - b
    print(f'Resultado: {subtracao:.2f}') 

def multiplicacao(a,b):
    multiplicar = a * b
    print(f'Resultado: {multiplicar:.2f}') 

def divisao(a,b):
    try:
        dividir = a / b
        print(f'Resultado: {dividir:.2f}')
    except ZeroDivisionError as e:
        print('Erro: Divisão por zero não é permitida.')

def calculadora(primeiro, operador, segundo):
    try:
        validador = ['+', '-', '*', '/']
        if operador not in validador:
            print('Entrada incorreta, operador deve ser (+, -, *, /)')
            return
        
        if operador == '+':
            somar(primeiro, segundo)
        elif operador == '-':
            subtratir(primeiro, segundo)
        elif operador == '*':
            multiplicacao(primeiro, segundo)
        else:
            divisao(primeiro, segundo)
            
    except ValueError:
        print('Erro: Entrada inválida. Digite apenas números.')


primeiro_numero = float(input('Digite o primeiro número: '))
operacao = input('Escolha a operação (+, -, *, /): ')
segundo_numero = float(input('Digite o segundo número: '))

calculadora(primeiro_numero, operacao, segundo_numero) 



'''SOLUCAO ALURA'''
# def somar(num1, num2):
#     return num1 + num2
 
# def subtrair(num1, num2):
#     return num1 - num2
 
# def multiplicar(num1, num2):
#     return num1 * num2
 
# def dividir(num1, num2):
#     if num2 == 0:
#         raise ZeroDivisionError
#     return num1 / num2
 
# def calculadora():
#     try:
#         num1 = float(input("Digite o primeiro número: "))
#         operacao = input("Escolha a operação (+, -, *, /): ")
#         num2 = float(input("Digite o segundo número: "))
 
#         if operacao == "+":
#             resultado = somar(num1, num2)
#         elif operacao == "-":
#             resultado = subtrair(num1, num2)
#         elif operacao == "*":
#             resultado = multiplicar(num1, num2)
#         elif operacao == "/":
#             resultado = dividir(num1, num2)
#         else:
#             print("Operação inválida!")
#             return
 
#         print(f"Resultado: {resultado}")
 
#     except ValueError:
#         print("Erro: Entrada inválida. Digite apenas números.")
#     except ZeroDivisionError:
#         print("Erro: Divisão por zero não é permitida.")
 
# calculadora()