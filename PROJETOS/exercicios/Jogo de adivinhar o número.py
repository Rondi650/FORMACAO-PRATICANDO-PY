# Maria está criando um jogo para seus alunos praticarem lógica e pensamento rápido. Ela quer um programa onde o computador escolhe um número aleatório entre 1 e 100, e o jogador tem que adivinhar qual é.

# Além de garantir a jogabilidade, Maria deseja que o programa trate erros de entrada, impedindo que o usuário forneça valores inválidos, como letras ou números fora do intervalo permitido.

# Sua tarefa é criar um programa que gere um número aleatório entre 1 e 100 e permita que o usuário tente adivinhar o número. O programa deve informar se o palpite é maior ou menor que o número correto, até que o usuário acerte. Se o usuário digitar um valor inválido ou um número fora do intervalo, uma exceção ValueError deve ser lançada .

import random, os
os.system('cls')

aleatorio = int(random.randrange(start=1,stop=101))
tentativas = 0
while True:
    try:
        entrada_usuario = int(input('Tente adivinhar o número (1-100): '))
        tentativas += 1
        if not 1 <= entrada_usuario <= 100:
            print('Entrada inválida: Número fora do intervalo! Digite um número entre 1 e 100.')
            continue
           
        if entrada_usuario < aleatorio:
            print(f'Muito baixo! Tente novamente: {entrada_usuario}')
        elif entrada_usuario > aleatorio:
            print(f'Muito alto! Tente novamente: {entrada_usuario}')
        else:
            print(f'Parabéns! Você acertou o número {aleatorio}, com {tentativas} tentativas.')
            break
        
    except ValueError as e:
        print(f'Entrada inválida: {e}')