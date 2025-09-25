# Nathalia é gerente de uma loja virtual e precisa de um sistema que receba os registros de vendas organizados por categoria de produto. Cada categoria contém uma lista de dicionários representando as vendas individuais, com informações sobre o produto, a quantidade vendida e o valor unitário. Sua tarefa é criar um programa que exiba o total de vendas por categoria.

# Saída esperada:
# Total de vendas por categoria: 
# - Eletrônicos: R$ 14500.00 
# - Eletrodomésticos: R$ 9200.00 
# - Livros: R$ 1000.00 

'''SOLUCAO RONDINELLE'''
import os
os.system('cls')

vendas = { 
    "Eletrônicos": [ 
        {"produto": "Smartphone", "quantidade": 5, "valor_unitario": 2000}, 
        {"produto": "Tablet", "quantidade": 3, "valor_unitario": 1500} 
    ], 
    "Eletrodomésticos": [ 
        {"produto": "Geladeira", "quantidade": 2, "valor_unitario": 3000}, 
        {"produto": "Micro-ondas", "quantidade": 4, "valor_unitario": 800} 
    ], 
    "Livros": [ 
        {"produto": "Livro A", "quantidade": 10, "valor_unitario": 50}, 
        {"produto": "Livro B", "quantidade": 5, "valor_unitario": 100} 
    ] 
} 

vendas_categoria = {}
for categorias, valores in vendas.items():
    total2 = 0
    for detalhes in valores:
        
        qtd = detalhes['quantidade']
        valor = detalhes['valor_unitario']
        total = qtd * valor
        total2 += (detalhes['quantidade']*detalhes['valor_unitario'])
        
        if categorias not in vendas_categoria:
            vendas_categoria[categorias] = []
        vendas_categoria[categorias].append(total)
    
    print(f'- {categorias}: R$ {total2:.2f}')
   
for i,x in vendas_categoria.items():
    print(f'- {i}: R$ {sum(x)}')



'''SOLUCAO ALURA'''
vendas = { 
    "Eletrônicos": [ 
        {"produto": "Smartphone", "quantidade": 5, "valor_unitario": 2000}, 
        {"produto": "Tablet", "quantidade": 3, "valor_unitario": 1500} 
    ], 
    "Eletrodomésticos": [ 
        {"produto": "Geladeira", "quantidade": 2, "valor_unitario": 3000}, 
        {"produto": "Micro-ondas", "quantidade": 4, "valor_unitario": 800} 
    ], 
    "Livros": [ 
        {"produto": "Livro A", "quantidade": 10, "valor_unitario": 50}, 
        {"produto": "Livro B", "quantidade": 5, "valor_unitario": 100} 
    ] 
} 

print("Total de vendas por categoria:") 
for categoria, itens in vendas.items(): 
    total = 0 
    for item in itens: 
        total += item["quantidade"] * item["valor_unitario"] 
    print(f"- {categoria}: R$ {total:.2f}") 