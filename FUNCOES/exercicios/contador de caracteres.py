# Sara está participando de um concurso de escrita, e uma das regras exige que cada palavra de seu texto tenha um limite máximo de caracteres.

# Ajude Sara criando uma função que receba uma palavra e exiba a quantidade de caracteres.

''''PROPOSTA RONDI'''
def contar_caracteres(palavra):
    soma = 0
    for x in palavra:
        tamanho = len(x)
        soma += tamanho
    print(f'A palavra {palavra} tem {soma} caracteres.')
    
palavra = str(input('Digite uma palavra: '))
contar_caracteres(palavra)

''''PROPOSTA ALURA'''
def contar_palavras2(nova_palavra):
    return print(f'A palavra {nova_palavra}, tem {len(nova_palavra)} caracteres.')

Outra_palavra = str(input('Digite uma palavra: '))
contar_palavras2(Outra_palavra)