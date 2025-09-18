# Carlos trabalha em um comércio e precisa saber o valor total de vendas realizadas no dia. As vendas são informadas em uma única linha separadas por espaços.

# Sua tarefa é criar um programa que receba essa linha, converta os valores para números e exiba o total.



'''RESOLUCAO RONDINELLE'''
def somar_vendas(vendas):
    apartar_dados = vendas.split()
    soma_inteiro = sum([float(venda) for venda in apartar_dados])
    return f'O total de vendas foi: {soma_inteiro}'

vendas = str(input('Digite os valores das vendas: '))
print(somar_vendas(vendas))


'''RESOLUCAO ALURA'''

valores = input("Digite os valores das vendas: ").split() 
total = sum(map(float, valores)) 
print(f"O total de vendas foi: {total}") 