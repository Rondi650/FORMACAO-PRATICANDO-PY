# Miguel está desenvolvendo um sistema de cupons de desconto e precisa de uma forma para aplicar diferentes taxas de desconto sobre os valores das compras.

# Diante deste problema, crie uma closure que gere uma função capaz de calcular o preço final com um desconto fixo definido pelo usuário.

'''SOLUCAO RONDINELLE'''
import os
os.system('cls')

def valor_desconto(y):
    def valor_compra(x):
        valor_final = x - (x * y/100)
        return f'Preço final com desconto: {valor_final}\n'
    return valor_compra

desconto = float(input('Digite a porcentagem de desconto: '))
compra = float(input('Digite o valor da compra: '))

retorno_desconto = valor_desconto(desconto)
print(retorno_desconto(compra))


'''SOLUCAO ALURA'''

def criar_desconto(porcentagem):  
   def calcular_preco(valor):  
       return valor - (valor * (porcentagem / 100))  
   return calcular_preco 

desconto = float(input("Digite a porcentagem de desconto: "))  
calcular_preco_final = criar_desconto(desconto) 
valor = float(input("Digite o valor da compra: "))  

print(f"Preço final com desconto: {calcular_preco_final(valor)}") 