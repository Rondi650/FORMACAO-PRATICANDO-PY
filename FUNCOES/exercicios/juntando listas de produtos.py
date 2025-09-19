# Clara está gerenciando o estoque de sua loja e recebeu duas listas separadas: uma contendo os nomes dos produtos e outras com seus respectivos preços. Para facilitar a organização, ela precisa combinar essas listas de forma que cada produto seja associado ao seu preço.

# Crie um programa que junte as listas e exiba o resultado no formato produto: preço
import os

'''SOLUCAO RONDINELLE'''
def saida_dados_frutas(dados_frutas,dados_precos_frutas):
    converte_float = list(map(float,dados_precos_frutas))
    zipado= dict(zip(dados_frutas, converte_float))
    for chave, valor in zipado.items():
        print(f'{chave.strip()}: {valor}')
     
frutas = str(input('Digite os produtos separados por vírgula: ')).split(',') # maçã, banana, pera  
precos_frutas = str(input('Digite os preços separados por vírgula: ')).split(',') # 2.5, 1.2, 3.0 

os.system('cls')

saida = saida_dados_frutas(frutas,precos_frutas)


'''SOLUCAO ALURA'''
produtos = input("Digite os produtos separados por vírgula: ").split(",") 
precos = input("Digite os preços separados por vírgula: ").split(",") 
 
for produto, preco in zip(produtos, precos): 
    print(f"{produto.strip()}: {preco.strip()}") 

