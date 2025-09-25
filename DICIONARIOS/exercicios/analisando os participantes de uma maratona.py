# Lucas é voluntário na organização de uma maratona e recebeu a lista de participantes com suas respectivas idades. Agora, ele precisa de um programa que apresente três informações:

# Os nomes de todos os participantes.
# As idades de todos os participantes.
# Uma relação completa com o nome e a idade de cada um.
# Sua tarefa é criar esse programa com base nas informações fornecidas.

'''SOLUCAO RONDINELLE'''
import os
os.system('cls')

participantes = { 
    "Mariana": 25, 
    "Carlos": 32, 
    "Beatriz": 28, 
    "Rafael": 35 
} 

nomes_lista = []
idades_lista = []

for nomes, idades in participantes.items():
    nomes_lista.append(nomes)
    idades_lista.append(str(idades))
    print(f'- {nomes}: {idades} anos')
    
print(f'Nomes dos participantes: ' + ', '.join(nomes_lista))
print(f'Idades dos participantes: ' + ', '.join(idades_lista))



'''SOLUCAO ALURA'''
participantes = { 
    "Mariana": 25, 
    "Carlos": 32, 
    "Beatriz": 28, 
    "Rafael": 35 
} 

print(f"Nomes dos participantes: {', '.join(participantes.keys())}") 
print(f"Idades dos participantes: {', '.join(str(idade) for idade in participantes.values())}") 
print("Participantes e suas idades:") 
for nome, idade in participantes.items(): 
    print(f"- {nome}: {idade} anos") 

