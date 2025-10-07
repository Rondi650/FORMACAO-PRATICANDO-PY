# Marcos é dono de uma loja online e precisa de um sistema que processe pedidos de forma assíncrona. O sistema deve seguir a seguinte lógica:

# Primeiro, verificar se o pagamento foi aprovado;
# Se o pagamento for aprovado, verificar se há estoque disponível;
# Somente se houver estoque disponível, confirmar o pedido e enviá-lo para entrega;
# Se o pagamento falhar ou não houver estoque, o pedido deve ser cancelado.
# A lista de pedidos já está definida no sistema, com o status do pagamento e do estoque previamente cadastrados. Confira o código:

pedidos = [
    {"id": 101, "pagamento_aprovado": True, "estoque_disponivel": True},
    {"id": 102, "pagamento_aprovado": True, "estoque_disponivel": False},
    {"id": 103, "pagamento_aprovado": False, "estoque_disponivel": True},
    {"id": 104, "pagamento_aprovado": True, "estoque_disponivel": True},
    {"id": 105, "pagamento_aprovado": False, "estoque_disponivel": False},
]

import asyncio, os
os.system('cls')

async def status_pedidos(pedido):
    print(f'\nProcessando pedido {pedido['id']}')
    if not pedido['pagamento_aprovado']:
        print(f'Pagamento recusado para pedido #{pedido['id']}. Pedido cancelado.')
        return
    else:
        print(f'Pagamento aprovado para pedido #{pedido['id']}')
        
    if not pedido['estoque_disponivel']:
        print(f'Estoque indisponível para pedido #{pedido['id']}. Pedido cancelado.')
        return
    else:
        print(f'Estoque disponível para pedido #{pedido['id']}.')
    
    if pedido['pagamento_aprovado'] and pedido['estoque_disponivel']:
        print(f'Pedido #{pedido['id']} confirmado! Enviado para entrega.')
        
async def main():
    tarefa = [asyncio.create_task(status_pedidos(pedido)) for pedido in pedidos]
    await asyncio.gather(*tarefa)
    print('\nTodos os pedidos foram processados!')
    
asyncio.run(main())