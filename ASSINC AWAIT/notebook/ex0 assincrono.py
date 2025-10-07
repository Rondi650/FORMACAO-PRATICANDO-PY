'''MODO ASSINCRONO'''
import asyncio

async def tarefa(numero):
    print(f"Iniciando tarefa {numero}.")
    await asyncio.sleep(2)
    print(f"Tarefa {numero} concluída!")
    
async def main():
    await asyncio.gather(tarefa(1),
tarefa(2), tarefa(3))
    
asyncio.run(main())