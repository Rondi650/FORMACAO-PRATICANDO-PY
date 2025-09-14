# Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C. No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos e não calcular o total.

# Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. Se algum valor for negativo, mostre uma mensagem informando o erro.

atividade_1 = int(input('Informe os dias para a atividade 1: '))
atividade_2 = int(input('Informe os dias para a atividade 2: '))
atividade_3 = int(input('Informe os dias para a atividade 3: '))
atividade_4 = int(input('Informe os dias para a atividade 4: '))

lista = [atividade_1, atividade_2, atividade_3]

def positivo():
    soma = 0
    lista.append(atividade_4)
    for i, numero in enumerate(lista):
        if numero < 0:
            print(f'Os dias nao podem ser negativos, atividade {i+1}: ({numero}), desconsiderada da somatoria.')
            numero = 0
        soma += numero 
    return print(f'Somatoria dos dias das atividades = {soma}')
            
positivo()

    

