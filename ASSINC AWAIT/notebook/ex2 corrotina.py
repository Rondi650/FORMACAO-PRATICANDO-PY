import asyncio, os
os.system('cls')

async def corrotina(numero):
    print(f'Iniciando tarefa {numero}')
    await asyncio.sleep(2)
    print(f'Tarefa {numero} concluida')
    
async def main():
    await corrotina(1)
    await corrotina(2)
    
asyncio.run(main())