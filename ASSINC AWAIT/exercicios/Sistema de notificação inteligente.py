# Lucas trabalha em um sistema de notificações que precisa enviar mensagens para usuários. No entanto, algumas notificações só devem ser enviadas se o usuário tiver ativado essa opção no sistema. Além disso, se o usuário for VIP, ele deve receber uma notificação prioritária antes das demais.

# Com base nesse cenário, crie um programa que simule o envio de notificações para três usuários. Cada usuário tem um status diferente:

# Ana: VIP (deve receber uma notificação prioritária antes das normais).
# João: Usuário comum, mas ativou as notificações.
# Carla: Usuária comum, mas desativou as notificações (não deve receber nada).
# O programa deve exibir quais notificações foram enviadas e quais usuários não receberam nada.

usuarios = [
    {"nome": "Ana", "vip": True, "notificacoes_ativadas": True},
    {"nome": "João", "vip": False, "notificacoes_ativadas": True},
    {"nome": "Carla", "vip": False, "notificacoes_ativadas": False},
]

import asyncio

async def enviar_notificacoes(usuario):
    if not usuario['notificacoes_ativadas']:
        print(f'Nao enviada notificacoes para {usuario['nome']}')
        return
        
    if usuario['vip']:
        print(f'Usuario {usuario['nome']} recebeu com prioridade.')
        return
        
    print(f'Notificacao normal enviada para {usuario['nome']} ')
        

async def main():
    tarefa = [asyncio.create_task(enviar_notificacoes(usuario)) for usuario in usuarios]
    await asyncio.gather(*tarefa)
    
asyncio.run(main())
        

