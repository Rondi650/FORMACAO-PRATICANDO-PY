# Uma escola está organizando os dados dos alunos para criar um relatório resumido. Cada aluno tem seus dados registrados em uma única entrada, incluindo nome, idade e nota final no semestre. Esses dados devem ser exibidos separadamente para cada aluno no formato abaixo:

# Ajude a escola a desenvolver um programa que registre as informações dos alunos, organize os dados e exiba um relatório detalhado com as informações separadamente.


'''SOLUCAO RONDINELLE'''
import os
os.system('cls')

dados = input('Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: ').strip().split(', ')
# João, 16, 8.5, Maria, 17, 9.2, Pedro, 15, 7.8

for i,x in enumerate(dados):
    if i % 3 == 0:
        print(i)
        print(f'Aluno: {x}\n'
              f'Idade: {int(dados[i+1])}\n'
              f'Nota: {float(dados[i+2])}\n')
    
        
'''SOLUCAO ALURA'''
dados = input("Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: ").split(", ")

for i in range(0, len(dados), 3):
    nome, idade, nota = dados[i], int(dados[i + 1]), float(dados[i + 2])
    print(f"Aluno: {nome}")
    print(f"Idade: {idade}")
    print(f"Nota: {nota}\n")