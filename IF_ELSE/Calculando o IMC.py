# Anna Júlia está criando um sistema para calcular o Índice de Massa Corporal (IMC) e fornecer recomendações básicas. O programa deve receber o peso e a altura de uma pessoa e exibir o valor do IMC, além de indicar se está abaixo do peso, com peso normal ou acima do peso. Crie um programa que receba o peso (em kg) e a altura (em metros) e calcule o IMC usando a fórmula: IMC = peso / (altura ** 2) Depois, exiba o valor do IMC e uma mensagem indicando se está abaixo do peso (IMC < 18.5), peso normal (18.5 <= IMC < 25) ou acima do peso (IMC >= 25).



peso = float(input('Digite o seu peso (kg): '))
altura = float(input('Digite a sua altura (m): '))

imc = peso / (altura*2)
print(f'Seu IMC e: {imc:.2f}')

if imc < 18.5:
    print('Voce esta abaixo do peso')
elif 18.5 <= imc < 25:
    print('Voce esta com peso normal')
else:
    print('Voce esta acima do peso') 

