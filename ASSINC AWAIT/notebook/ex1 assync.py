import asyncio

async def corrotina():
    print('Inicio')
    await asyncio.sleep(2)
    print('Fim')
    
asyncio.run(corrotina())

