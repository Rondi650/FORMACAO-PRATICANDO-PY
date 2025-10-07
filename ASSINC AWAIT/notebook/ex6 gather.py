import asyncio

async def corrotina(nome, tempo):
    print(f"Tarefa {nome} iniciada.")
    await asyncio.sleep(tempo)
    print(f"Tarefa {nome} concluída.")
    
async def main():
    await asyncio.gather(
        corrotina("1",2),
        corrotina("2",3),
        corrotina("3",1)
        )

asyncio.run(main())
