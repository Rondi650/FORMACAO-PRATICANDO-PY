# João trabalha como garçom em um restaurante e precisa calcular a gorjeta que os clientes deixam ao pagar a conta. O restaurante sugere uma gorjeta de 10%, mas alguns clientes podem escolher dar mais ou menos.

# Para agilizar o processo, João quer um programa que receba o valor total da conta e a porcentagem de gorjeta desejada e exiba o valor final que o cliente deverá pagar.

# Crie um programa que peça ao usuário o valor da conta e a porcentagem de gorjeta. O programa deve calcular e exibir o valor da gorjeta e o total a ser pago.

'''PROPOSTA RONDI'''
conta = float(input('Digite o valor da conta: '))
porcentagem = float(input('Digite a porcentagem de gorjeta: '))

def gorjeta(conta, porcentagem):
    valor = conta * (porcentagem/100)
    total = valor + conta
    print(f'Valor da gorjeta: R${valor:.2f}\n'
          f'Total a pagar: R${total:.2f}')
    
gorjeta(conta,porcentagem)


'''RESPOSTA ALURA'''
valor_conta = float(input("Digite o valor da conta: ")) 
porcentagem_gorjeta = float(input("Digite a porcentagem de gorjeta: ")) 
gorjeta2 = (porcentagem_gorjeta / 100) * valor_conta 
total_a_pagar = valor_conta + gorjeta2 
print(f"Valor da gorjeta: R$ {gorjeta2:.2f}") 
print(f"Total a pagar: R$ {total_a_pagar:.2f}")