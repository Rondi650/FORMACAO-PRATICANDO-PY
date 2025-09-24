# Laura e Ana resolveram fazer compras juntas, mas criaram duas listas diferentes. Elas querem um programa que mostre:

# Quais itens apareceram nas duas listas
# Quais foram exclusivos de Laura
# Quais foram exclusivos da Ana

# Escreva um programa que solicite as listas e mostre os resultados dessas comparações.

'''SOLUCAO RONDINELLE'''
import os
os.system('cls')

lista1 = set(input('Lista de Laura: ').strip().lower().split(', ')) # leite, pão, café, açúcar 
print(lista1)
lista2 = set(input('Lista de Ana: ').strip().lower().split(', ')) # pão, café, biscoito, chocolate 
print(lista2)

# Itens em ambas as listas: pão, café 
ambas = lista1 & lista2
print(f'Itens em ambas as listas: {', '.join(ambas)}')

# Itens exclusivos de Laura: leite, açúcar 
exclusivos_lista1 = lista1 - lista2
print(f'Itens exclusivos de Laura: {', '.join(exclusivos_lista1)}')

# Itens exclusivos de Ana: biscoito, chocolate 
exclusivos_lista2 = lista2 - lista1
print(f'Itens exclusivos de Ana: {', '.join(exclusivos_lista2)}')



# '''SOLUCAO ALURA'''
# laura = set(input("Lista da Laura: ").split(", "))  
# ana = set(input("Lista da Ana: ").split(", "))  

# comuns = laura.intersection(ana)  
# exclusivos_laura = laura.difference(ana)  
# exlusivos_ana = ana.difference(laura)  

# print(f"Itens em ambas as listas: {', '.join(comuns)}")  
# print(f"Itens exclusivos de Laura: {', '.join(exclusivos_laura)}")  
# print(f"Itens exclusivos de Ana: {', '.join(exlusivos_ana)}") 