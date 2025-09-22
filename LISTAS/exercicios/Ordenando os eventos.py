# A Futuro Eventos, uma empresa especializada em organização de conferências, cometeu um erro ao registrar a sequência dos eventos de uma conferência importante. Os eventos foram registrados na ordem inversa à que deveriam acontecer. Agora, a equipe precisa corrigir a ordem dos eventos para garantir que a conferência aconteça conforme o planejamento original.

# Considerando a lista inicial de eventos, crie um programa que permita ao organizador ordená-los, de forma que a lista final siga a sequência correta.


'''SOLUCAO RONDINELLE'''
eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']

def menu_inicial():
    print(f'Lista Atual: {eventos_registrados}')
    opcao = (input('Digite 1 para incluir um novo dado na lista.\n'
                    'Digite 2 para editar os dados da lista.\n'
                    'Digite outra tecla para sair do sistema.\n'
                    'Digitar: '))
    if opcao == '1':
        incluir(eventos_registrados)
    if opcao == '2':
        editar(eventos_registrados)
    else:
        import os
        os.system('cls')

def incluir(eventos):
    while True:
        item = input('Digite o nome do item que deseja ordenar: ')
        ordem = int(input('Digite a ordem que deseja incluir: '))
        eventos.insert(ordem - 1 , item)
        print(f'Lista Ordenada: {eventos}')
        
        continuar = input('Deseja incluir mais items? (S/N): ')
        validacao_sim = ['S','s','sim','Sim','SIM']
        
        if continuar in validacao_sim:
            continue
        else:
            menu_inicial()
            break
        
def editar(eventos):
    while True:
        item = input('Digite o nome do item que deseja ordenar: ')
        eventos.remove(item)
        ordem = int(input('Digite a ordem que deseja incluir: '))
        eventos.insert(ordem -1 , item)
        print(f'Lista Ordenada: {eventos}')
        
        continuar = input('Deseja ordenar mais items? (S/N): ')
        validacao_sim = ['S','s','sim','Sim','SIM']
        
        if continuar in validacao_sim:
            continue
        else:
            menu_inicial()
            break
 
def main():
    menu_inicial()
 
if __name__ == "__main__":
    main()
    
    
'''SOLUCAO ALURA'''
eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']

eventos_registrados.reverse()
print(f"Ordem corrigida: {eventos_registrados}")