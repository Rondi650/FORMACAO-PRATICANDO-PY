# Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado. Ele registrou a quantidade vendida de dois produtos: maçãs e bananas. Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda.

# Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.


macas = int(input('Digite a quantidade de macas vendidas: '))
bananas = int(input('Digite a quantidade de bananas venvidas: '))

if macas > bananas:
    print(f'As macas tiveram mais vendas: {macas} ante {bananas}.')
elif macas < bananas:
    print(f'As bananas tiveram mais vendas: {bananas} ante {macas}.')
else:
    print(f'As macas e bananas tiveram a mesma quantidade de vendas: {macas} de cada.')
        