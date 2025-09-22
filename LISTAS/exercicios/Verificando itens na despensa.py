# Roberto está organizando sua despensa e quer verificar se determinados itens já estão armazenados antes de adicioná-los à lista de compras.

# Ajude Roberto a criar um programa que pergunte o item desejado e verifique se ele está na lista de itens disponíveis na despensa. Caso o item não esteja na lista, o programa deve informar que ele precisa ser comprado.

'''PROPOSTA RONDINELLE'''
import os

lista = ['milho', 'arroz', 'vinagre']
        
def verificar_disponibilidade():
    digitado = input('Digite o item que você quer verificar: ')
    
    if digitado in lista:
        print(f'O item {digitado} já está na despensa.')
    else:
        print(f'O item {digitado} não está na despensa.')
        
        while True:
            adicionar = input('Deseja adicioná-lo na despensa? (S/N): ')
            
            validacao_sim = ['S','s','sim','Sim','SIM']
            validacao_nao = ['N','n','nao','Nao','NAO']
            
            if adicionar in validacao_sim:
                lista.append(digitado)
                break
            elif adicionar in validacao_nao:
                break
            else:
                print('Digite um valor válido (S/N)')
                continue
            
def verificar_despensa(x):
    print('DESPENSA ATUAL')
    for i, item in enumerate(x):
        print(f'{i+1} - {item}')
    
def adicionar():
    adicionar = input('Deseja verificar mais itens? (S/N): ')
    validacao = ['S','s','sim','Sim','SIM']
    if adicionar in validacao:
        main()
    else:
        os.system('cls')

def main():
    verificar_disponibilidade()
    verificar_despensa(lista)
    adicionar()
    
main()


'''PROPOSTA ALURA'''
despensa = ['arroz', 'feijão', 'óleo']
item = input("Digite o item que você quer verificar: ")
if item in despensa:
    print(f"O item {item} já está disponível na despensa.")
else:
    print(f"O item {item} precisa ser comprado.")
print(despensa)