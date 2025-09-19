# Joana está participando de um processo seletivo para uma vaga de desenvolvedora e recebeu um desafio técnico de criar uma calculadora para somar, subtrair, multiplicar e dividir dois números.

# Sua tarefa é criar um programa usando funções lambda que receba dois números e um operador matemático escolhido pelo usuário (+, -, * ou /) e exiba o resultado correspondente.

'''SOLUCAO RONDINELLE'''
import os

operacao = str(input('Escolha a operação (| + | - | * | / |): '))

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

os.system('cls')

if operacao == '+':
    soma = lambda a,b : a+b 
    print(f'{n1} + {n2} = {soma(n1,n2):.2f}\n')
elif operacao == '-':
    subtracao = lambda a,b : a-b
    print(f'{n1} - {n2} =  {subtracao(n1,n2):.2f}\n')
elif operacao == '*':
    multiplicacao = lambda a,b : a*b
    print(f'{n1} * {n2} =  {multiplicacao(n1,n2):.2f}\n')
elif operacao == '/':
    try:
        divisao = lambda a,b : a/b
        print(f'{n1} / {n2} =  {divisao(n1,n2):.2f}\n')
    except ZeroDivisionError:
        print(f'A divisao nao pode ter denominador zero.\n')
else:
    print(f'Digite um operador matematico valido: | + | - | * | / | \n')



'''SOLUCAO ALURA'''
soma = lambda x, y: x + y 
subtrai = lambda x, y: x - y 
multiplica = lambda x, y: x * y 
divide = lambda x, y: x / y if y != 0 else "Erro: Divisão por zero" 

x = float(input("Digite o primeiro número: ")) 
y = float(input("Digite o segundo número: ")) 
operacao = input("Escolha a operação (| + | - | * | / |): ") 
 
if operacao == '+': 
    print(f"O resultado é: {soma(x, y)}") 
elif operacao == '-': 
    print(f"O resultado é: {subtrai(x, y)}") 
elif operacao == '*': 
    print(f"O resultado é: {multiplica(x, y)}") 
elif operacao == '/': 
    print(f"O resultado é: {divide(x, y)}") 
else: 
    print("Operação inválida") 