# Ana é responsável pelo controle de estoque de uma loja de artigos para papelaria. Ela precisa de um programa que permita cadastrar produtos em forma de dados estruturados. O sistema deve solicitar o nome e a quantidade de três produtos e, ao final, exibir as informações cadastradas em um dicionário, onde cada produto será uma chave e a quantidade correspondente será o valor.

# dicionario = {}

# while True:
#     nome = input('Digite o nome do produto: ').strip()
#     qtd= input('Digite a quantidade: ')
    
#     dicionario[nome] = qtd
#     print('\nDicionário de produtos:\n'
#         f'{dicionario}\n')
            
#     adicionar = input('Deseja adicionar mais items? (S/N): ')
#     if adicionar.lower() == 's':
#         continue
#     elif adicionar.lower() == 'n':
#         import os
#         os.system('cls')
#         break  
#     else:
#         print('Dados incorreto, entrada deve ser S ou N.')
 
'''SOLUCAO RONDINELLE'''
import os
os.system('cls')

dicionario = {}

def adicionar_produtos(adicionar):
    nome = input('Digite o nome do produto: ').strip()
    qtd= input('Digite a quantidade: ')           
    adicionar[nome] = qtd
    print('\nDicionário de produtos:\n' f'{adicionar}\n')
    
adicionar_produtos(dicionario)

while True:
    adicionar = input('Deseja adicionar mais items? (S/N): ')
    if adicionar.lower() == 's':
        adicionar_produtos(dicionario)
        continue
    elif adicionar.lower() == 'n':
        print('\nLista Final:')
        for i,x in dicionario.items():
                print(f'{i} - {x}')
        print('\nSAINDO DO PROGRAMA... \n')
        break  
    else:
        print('Dados incorreto, entrada deve ser S ou N.')
        

# '''SOLUCAO ALURA'''
# dicionario_produtos = {} 

# for i in range(3): 
#     nome = input("Digite o nome do produto: ") 
#     quantidade = int(input("Digite a quantidade: ")) 
#     dicionario_produtos[nome] = quantidade 

# print(f"Dicionário de produtos: {dicionario_produtos}") 