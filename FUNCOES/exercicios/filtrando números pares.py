# Lucas está desenvolvendo um sistema para gerar relatórios financeiros e precisa filtrar apenas os valores pares de uma lista de números informada pelo usuário.

# Crie um programa que receba uma lista de números e exiba apenas os pares usando a função filter().

'''SOLUCAO RONDINELLE'''
def numeros_pares(lista_numeros):
    transformar_em_numero = list(map(int , lista_numeros))
    dados_filtrados = list(filter(lambda x: x % 2 == 0 , transformar_em_numero))
    transformar_em_texto = list(map(str , dados_filtrados))
    saida_em_texto = ' '.join(transformar_em_texto)
    return print(f'Números pares: {saida_em_texto}')

digitar = input('Digite os números separados por espaço: ').split()
numeros_pares(digitar)


'''SOLUCAO ALURA'''
numeros = input("Digite os números separados por espaço: ").split() 
pares = filter(lambda x: int(x) % 2 == 0, numeros) 
print("Números pares:", " ".join(pares)) 