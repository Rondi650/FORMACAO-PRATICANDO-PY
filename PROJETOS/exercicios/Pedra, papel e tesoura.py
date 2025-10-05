# Lucas quer criar um jogo de pedra, papel e tesoura para jogar contra o computador. Ele precisa de um programa que permita ao usuário escolher uma opção e depois exiba o resultado da partida.

# Crie um programa que permita ao usuário escolher entre pedra, papel ou tesoura. O computador escolherá aleatoriamente uma opção. O programa deve exibir quem venceu a partida. Lembrando que:

# Pedra ganha de Tesoura (Pedra quebra Tesoura);
# Tesoura ganha de Papel (Tesoura corta Papel);
# Papel ganha de Pedra (Papel cobre Pedra);
# Se ambos escolherem a mesma opção, é um empate. 

'''SOLUCAO RONDI'''
import random, os
os.system('cls')

escolha = ['pedra','papel','tesoura']
escolha_computador = random.choice(escolha)

def pedra_papel_tesoura(computador, usuario):
    print(f'Computador escolheu: {computador}')

    if usuario == 'pedra' and computador == 'tesoura':
        print('Pedra quebra Tesoura, Você venceu!')
    elif usuario == 'tesoura' and computador == 'papel':
        print('Tesoura corta Papel, Você venceu!')
    elif usuario == 'papel' and computador == 'pedra':
        print('Papel cobre Pedra, Você venceu!')
    elif usuario == computador:
        print('Empate')
    else:
        print('Vocë perdeu.')

escolha_usuario = input('Escolha: pedra, papel ou tesoura? ').lower()
if escolha_usuario not in escolha:
    print('Dados invalidos, digite: pedra, papel ou tesoura.')
else:
    pedra_papel_tesoura(escolha_computador, escolha_usuario)
    
    
    
'''SOLUCAO OFICIAL ALURA'''
import random 
def pedra_papel_tesoura():
opcoes = ["pedra", "papel", "tesoura"] 
escolha_computador = random.choice(opcoes) 
escolha_usuario = input("Escolha: pedra, papel ou tesoura? ").lower() 

if escolha_usuario not in opcoes: 
    print("Escolha inválida!") 
    return 

print(f"Computador escolheu: {escolha_computador}") 

if escolha_usuario == escolha_computador: 
    print("Empate!") 
elif ( 
    (escolha_usuario == "pedra" and escolha_computador == "tesoura") or 
    (escolha_usuario == "papel" and escolha_computador == "pedra") or 
    (escolha_usuario == "tesoura" and escolha_computador == "papel") 
): 
    print("Você venceu!") 
else: 
    print("Você perdeu!") 
 
pedra_papel_tesoura()
