# Pedro está criando um sistema de cadastro de produtos para sua loja e percebeu que todos os números de telefone dos clientes estão armazenados como strings. No entanto, para facilitar buscas e validações, ele precisa que esses números sejam tratados como inteiros.

# Dado o seguinte código com uma lista de números de telefone armazenados incorretamente como str, faça duas funções, uma que converte os tipos para inteiro e outra que verifica se a conversão foi feita corretamente e todos os números de telefone são inteiros:

'''RESOLUCAO RONDINELLE'''
def alternan_para_int(numeros):
    lista = []
    for i, numero in enumerate(numeros):
        if isinstance(numero, bool):
            print(f'\nItem da lista de numero {i+1}, nao pode ser tipo booleano.')
            continue
        try:
            inteiro = int(numero)
            lista.append(inteiro)
        except Exception as e:
            print(f'Item da lista de numero {i+1}, erro: {e}')
            continue
    return lista
   
telefones = ["11987654321", False, "31987654321", None , '31995947349']    

def verificacao_int(x):
    nova_lista = (alternan_para_int(x))
    for numero in nova_lista:
        if not isinstance(numero,int):
            return 'Erro na conversao'
    return f'\nTodos os números foram convertidos corretamente! {nova_lista}\n'
    
     
print(verificacao_int(telefones))

'''LIST COMPREHENSION'''
def alteracao(x):
   print([int(y) for y in x])

# alteracao(telefones)



'''RESOLUCAO EXERCICIO ALURA'''
telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 
def converter_telefones(lista):  

   return [int(telefone) for telefone in lista] 

def verifica_tipos(lista):  

   for num in lista:  

       if not isinstance(num, int):  

           return "Erro na conversão."  

   return "Todos os números foram convertidos corretamente!" 

telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 

telefones_convertidos = converter_telefones(telefones) 

print(verifica_tipos(telefones_convertidos)) 
    

    

