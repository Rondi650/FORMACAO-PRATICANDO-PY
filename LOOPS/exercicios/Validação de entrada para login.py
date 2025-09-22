# João está desenvolvendo um sistema de cadastro para um site de leitura. Ele precisa garantir que os usuários insiram um nome de usuário e uma senha válidos. As regras são as seguintes:

# O nome de usuário deve ter pelo menos 5 caracteres.
# A senha deve ter pelo menos 8 caracteres.
# João quer que o sistema continue solicitando as informações até que ambas as condições sejam atendidas. Quando o usuário insere dados válidos, o programa deve exibir a mensagem: "Cadastro realizado com sucesso!".

# Crie um programa que implemente essa lógica usando um laço while.

# '''SOLUCAO RONDINELLE'''
# usuario = str(input('\n' + 'Digite o nome de usuario: '))

# while len(usuario) < 5:
#     print('O nome de usuario deve ter pelo menos 5 caracteres.')
#     novo_usuario = str(input('Digite o nome de usuario: '))
#     if len(novo_usuario) >=5:
#         usuario = novo_usuario
#         break
    
# print(f'Nome de usuario {usuario} aceito.')

# senha = str(input('Digite sua senha: '))

# while len(senha) < 8:
#     print('A senha deve ter pelo menos 8 caracteres.')
#     nova_senha = str(input('Digite sua senha: '))
#     if len(nova_senha) >= 8:
#         senha = nova_senha
#         break
    
# print('\n' + 'Cadastro realizado com sucesso.' + '\n' f'Bem vindo {usuario}!' + '\n')
# print(senha)


'''SOLUCAO WHILE TRUE'''

import os

tentativas = 0
tentativas_senha = 0
cadastro_completo = False

while True:
    usuario = str(input('\n' + 'Digite o nome de usuario: '))
    if len(usuario) < 5:
        print('O nome de usuario deve ter pelo menos 5 caracteres.')
        tentativas +=1
        if tentativas >= 3:
            print(f'Tentativas esgotadas {tentativas}')
            break
        continue
    
    while True:
        senha = str(input('Digite sua senha: '))
        if len(senha) < 3:
            print('A senha deve ter pelo menos 3 caracteres.') 
            tentativas_senha += 1
            if tentativas_senha >= 3:
                print(f'Tentativas esgotadas {tentativas_senha}')
                break
            continue
        
        confirmar_senha = str(input('Confirme sua senha: '))
        if confirmar_senha != senha:
            print('As senhas devem coincidir')
            continue
        
        cadastro_completo = True
        break
    
    break

if cadastro_completo:
    print('\n' + 'Cadastro realizado com sucesso.' + '\n' f'Bem vindo {usuario}!' + '\n')
else:
    print('Cadastro não foi concluído.')