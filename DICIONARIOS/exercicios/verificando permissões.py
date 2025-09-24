# Marina trabalha no setor de segurança de uma empresa e precisa verificar se um determinado conjunto de permissões faz parte das permissões principais de um sistema. Sua tarefa é desenvolver um programa que receba duas listas de permissões e verifique se a segunda lista está contida na primeira.

'''SOLUCAO RONDINELLE'''
import os
os.system('cls')

lista1 = set(item.strip() for item in input('Permissões principais: ').lower().split(', ')) # leitura, escrita, execução, compartilhamento 
print(lista1)
lista2 = set(item.strip() for item in input('Permissões solicitadas: ').lower().split(', ')) # leitura, escrita  |    leitura, exclusão
print(lista2)

comprehension = [i in lista1 for i in lista2]
    
if all(comprehension):
    print('As permissões solicitadas fazem parte das permissões principais.') 
else:
    print('As permissões solicitadas não fazem parte das permissões principais.')
    
    
print('com acesso') if lista2 <= lista1 else print('sem acesso')


# '''SOLUCAO ALURA'''
# permissoes_principais = set(input("Permissões principais: ").strip().lower().split(',')) 
# permissoes_solicitadas = set(input("Permissões solicitadas: ").strip().lower().split(',')) 

# for i in range(len(permissoes_principais)):  
#     permissoes_principais[i] = permissoes_principais[i].strip() 

# for i in range(len(permissoes_solicitadas)):  
#     permissoes_solicitadas[i] = permissoes_solicitadas[i].strip() 

# eh_subconjunto = permissoes_solicitadas.issubset(permissoes_principais) 
# if eh_subconjunto:  
#     print("As permissões solicitadas fazem parte das permissões principais.")  
# else:  
#     print("As permissões solicitadas não fazem parte das permissões principais.") 