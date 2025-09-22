# O clube de atletismo Alura Runners organizou uma corrida e divulgou a lista com a classificação final dos participantes. Mas, um erro foi identificado: um dos nomes está incorreto. O organizador precisa de um programa que permita localizar o nome errado e substituí-lo pelo correto.

# Como você escreveria um programa que solicite o nome errado, o nome correto e atualize a lista exibindo a nova classificação ao final?

'''SOLUCAO RONDINELLE'''
lista = ['Ana', 'Samara', 'Pedro']
print(lista)

incorreto = input('Digite o nome incorreto: ')

if incorreto in lista:
    for i, nome in enumerate(lista):
        if nome == incorreto:
            correto = input('Digite o nome correto: ')
            lista.pop(i)
            lista.insert(i,correto)
            print(f'O nome {incorreto} foi substituído por {correto}.')
            print(lista)
            break
else:
    print('Nome nao encontrado')
        
        
'''SOLUCAO ALURA'''
resultados = ["Ana", "Carlos", "Pedro"]
print("Lista original:", resultados)

erro = input("Digite o nome incorreto: ")
if erro in resultados:
    correto = input("Digite o nome correto: ")
    posicao = resultados.index(erro)
    resultados.remove(erro)
    resultados.insert(posicao, correto)
    print(f"O nome {erro} foi substituído por {correto}.")
    print("Lista atualizada:", resultados)
else:
    print("Nome não encontrado.")