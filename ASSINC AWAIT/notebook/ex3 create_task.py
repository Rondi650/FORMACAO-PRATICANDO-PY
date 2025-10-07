import asyncio, os
os.system('cls')

async def corrotina(numero):
    print(f'Iniciando tarefa {numero}')
    await asyncio.sleep(2)
    print(f'Tarefa {numero} concluida')
    
async def main():
    tarefa1 = asyncio.create_task(corrotina(1))
    tarefa2 = asyncio.create_task(corrotina(2))
    await tarefa1
    await tarefa2
    
asyncio.run(main())
