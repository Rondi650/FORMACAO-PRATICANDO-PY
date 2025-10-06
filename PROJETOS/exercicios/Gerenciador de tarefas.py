# Ana precisa de um programa simples para gerenciar suas tarefas diárias. Ela quer poder adicionar, visualizar e remover tarefas de uma lista.

# Crie um programa com um menu interativo que permita ao usuário adicionar, visualizar e remover tarefas. Use uma lista para armazenar as tarefas.

'''PROPOSTA RONDI'''
import os, sys

tarefas = []

def adicionar_tarefa():
    adicionar = input('Digite a tarefa: ').strip()
    tarefas.append(adicionar)
    print(f'Tarefa {adicionar} adicionada!')
    
def visualizar_tarefas():
    print('\nTAREFAS LISTADAS')
    if tarefas:
        for i, tarefa in enumerate(tarefas):
            print(f"{i+1} - {tarefa}")
    else:
        print('Sem tarefas para listar')  
    
def remover_tarefa():
    if tarefas:
        visualizar_tarefas()
        excluir_tarefa = int(input('\nDigite o número da tarefa a ser removida: ')) -1
        tarefa_excluida = tarefas.pop(excluir_tarefa)
        print(f"Tarefa {tarefa_excluida} removida!")
    else:
        print('Nenhuma tarefa para remover.')

def sair():
    os.system('cls')
    print('Saindo do gerenciador de tarefas. Até mais!')
    sys.exit()
    
def menu():
    while True:
        try:
            opcoes = int(input(
                    '\n1. Adicionar tarefa\n'
                    '2. Visualizar tarefas\n'
                    '3. Remover tarefa\n'
                    '4. Sair\n'
                    'Escolha uma opção: '
                    ))
            print()
            if opcoes == 1:
                adicionar_tarefa()
                continue
            elif opcoes == 2:
                visualizar_tarefas()
                continue
            elif opcoes == 3:
                remover_tarefa()
                continue
            elif opcoes == 4:
                sair()
                break
            else:
                print('Erro: Opção inválida! Escolha uma opção entre 1 e 4.')
        except ValueError:
            print('Erro: Opção inválida! Escolha uma opção entre 1 e 4.')
                    
menu()


'''PROPOSTA ALURA'''
def gerenciador_tarefas():
    tarefas = []
 
    while True:
        print("\n1. Adicionar tarefa")
        print("2. Visualizar tarefas")
        print("3. Remover tarefa")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
 
        if opcao == "1":
            tarefa = input("Digite a tarefa: ").strip()
            if tarefa:  # Verifica se a string não está vazia
                tarefas.append(tarefa)
                print("Tarefa adicionada!")
            else:
                print("Erro: A tarefa não pode estar vazia.")
 
        elif opcao == "2":
            if tarefas:
                print("\nTarefas:")
                for i, tarefa in enumerate(tarefas, 1):
                    print(f"{i}. {tarefa}")
            else:
                print("Nenhuma tarefa cadastrada.")
 
        elif opcao == "3":
            if not tarefas:
                print("Erro: Nenhuma tarefa para remover.")
                continue
 
            try:
                indice = int(input("Digite o número da tarefa a ser removida: ")) - 1
                if 0 <= indice < len(tarefas):
                    removida = tarefas.pop(indice)
                    print(f"Tarefa '{removida}' removida!")
                else:
                    print("Erro: Índice inválido! Digite um número válido.")
            except ValueError:
                print("Erro: Entrada inválida! Digite um número.")
 
        elif opcao == "4":
            print("Saindo do gerenciador de tarefas. Até mais!")
            break
 
        else:
            print("Erro: Opção inválida! Escolha uma opção entre 1 e 4.")
 
gerenciador_tarefas()