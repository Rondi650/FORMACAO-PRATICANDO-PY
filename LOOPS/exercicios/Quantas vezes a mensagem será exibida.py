# Marcos está desenvolvendo um programa para exibir uma mensagem de boas-vindas repetidamente no console, como parte de uma campanha de marketing de sua plataforma chamada Buscante. Ele quer garantir que a mensagem seja exibida 5 vezes.

# Ajude Marcos a escrever um programa que exiba a mensagem: "Bem-vindo ao Buscante!" o número exato de vezes que ele precisa.

contador = 0

while contador < 5:
    print(f"WHILE {contador + 1}: Bem-vindo ao Buscante!" )
    contador += 1
    

for numero in range(1,6):
    print(f"FOR {numero}: Bem-vindo ao Buscante!" )