# Joana é gerente de projetos e precisa consolidar as listas de tarefas de duas equipes distintas. Após unir as listas, ela quer remover uma tarefa específica informada pelo usuário. Sua tarefa é criar um programa que realize essa operação.

'''SOLUCAO RONDINELLE'''
equipe_a = {"planejar reunião", "revisar documento", "testar sistema"} 
equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"} 
tarefas = equipe_a | equipe_b

def mostrar_tarefas(x):
    print(f'-' * 50)
    print('TAREFAS:')
    for i, x in enumerate(x):
        print(f'{i+1} - {x}')
    print(f'-' * 50)
    
mostrar_tarefas(tarefas)

# print(f'\nTarefas atuais: \n{', '.join(tarefas)}\n')

while True:
    digitado = input('Digite A para adicionar uma tarefa.\n' 
                    'Digite D para deletar uma tarefa.\n' 
                    'Digite sair para sair.\n'
                    'Digitar: ')
        
    if digitado.lower() == 'a':
        adicionar = input('Digite a tarefa que deseja adicionar: ')
        tarefas.add(adicionar)
        mostrar_tarefas(tarefas)
            
    elif digitado.lower() == 'd':
        deletar = input('Digite a tarefa que deseja deletar: ')
        tarefas.discard(deletar)
        mostrar_tarefas(tarefas)
        
    elif digitado.lower() == 'sair':
        import os
        os.system('cls')
        break
    else:
        print('Digite um numero valido')
        
# '''SOLUCAO ALURA'''
# equipe_a = {"planejar reunião", "revisar documento", "testar sistema"}  
# equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"}  

# tarefas_combinadas = equipe_a.union(equipe_b) 
# tarefa_remover = input("Tarefa a ser removida: ").lower()  

# if tarefa_remover in tarefas_combinadas:  
#     tarefas_combinadas.remove(tarefa_remover) 

# print(f"Tarefas finais: {tarefas_combinadas}") 