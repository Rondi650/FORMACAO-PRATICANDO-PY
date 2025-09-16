# André está testando um novo recurso no backend do Buscante que processa dados em um loop. Durante os testes, ele percebeu que o sistema parou de responder, e suspeita que o problema está em um loop infinito.

contador = 0

while contador < 10:
    print(f"Processando dados... {contador}")
    contador += 1 # sem o incremento, o loop vai ser sempre True, ja que 0 e menor que 10