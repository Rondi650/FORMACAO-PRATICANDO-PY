# Paulo está desenvolvendo um programa para calcular valores acumulados em um sistema financeiro. Ele precisa somar os todos os números inteiros de 1 até n, onde n é um valor escolhido pelo usuário.

# Ajude Paulo criando uma função recursiva que receba um número n e retorne a soma de todos os números inteiros de 1 até N.

'''SOLUCAO RONDINELLE'''
def somatoria(input):
    somar = 0
    original = input
    while input >= 1:
        somar += input
        input -=1
    print(f'A soma de 1 a {original} é: {somar}')
    
numero = int(input('Digite um número: '))
somatoria(numero)


'''SOLUCAO ALURA'''
def soma_recursiva(n): 
    if n == 1: 
        return 1 
    return n + soma_recursiva(n - 1) 
 
numero2 = int(input("Digite um número: ")) 
print(f"A soma de 1 a {numero2} é: {soma_recursiva(numero2)}") 