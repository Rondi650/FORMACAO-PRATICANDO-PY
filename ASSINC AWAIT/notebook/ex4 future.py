import asyncio

import asyncio

async def corrotina(futuro):
    print('Corrotina: Início')
    await asyncio.sleep(2)
    print('Corrotina: Definindo resultado do Future para "Fim"')
    futuro.set_result('Fim')
    print('Corrotina: Finalizada')

async def main():
    print('Main: Criando Future')
    futuro = asyncio.Future()
    print('Main: Criando tarefa corrotina')
    asyncio.create_task(corrotina(futuro))
    print('Main: Aguardando resultado do Future')
    resultado = await futuro
    print(f'Main: Resultado recebido do Future: {resultado}')
    print('Main: Finalizada')

asyncio.run(main())