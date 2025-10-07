import asyncio

async def corrotina1(futuro):
    print("Tarefa 1 iniciada.")
    await asyncio.sleep(2)
    futuro.set_result("Resultado da Tarefa 1")
    print("Tarefa 1 finalizada.")

async def corrotina2(futuro):
    print("Tarefa 2 iniciada, aguardando o futuro.")
    resultado = await futuro
    print("Tarefa 2 finalizada com o resultado:", resultado)

async def main():
    print("Main: Criando Future e tarefas")
    futuro = asyncio.Future()
    tarefa1 = asyncio.create_task(corrotina1(futuro))
    tarefa2 = asyncio.create_task(corrotina2(futuro))
    print("Main: Aguardando tarefas")
    await tarefa1
    await tarefa2
    print("Main: Todas as tarefas finalizadas.")

asyncio.run(main())