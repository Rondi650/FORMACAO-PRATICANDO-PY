# Julia é professora e precisa de um programa para ajudar seus alunos a calcularem suas idades com base no ano de nascimento. Sua tarefa é criar uma função que receba o ano de nascimento e o ano atual e retorne à idade correspondente.

nascimento = int(input('Digite o ano de nascimento: '))
atual = int(input('Digite o ano atual: '))

def calcular_idade(ano_nascimento, ano_atual):
    return print(f'Sua idade: {ano_atual - ano_nascimento}')

calcular_idade(nascimento,atual)