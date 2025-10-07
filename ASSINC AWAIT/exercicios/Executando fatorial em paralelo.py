# Carlos precisa calcular o fatorial de cinco números diferentes simultaneamente. Como cálculos pesados podem demorar, ele quer garantir que todos sejam processados ao mesmo tempo, e os resultados exibidos assim que estiverem prontos.

# Crie um programa que calcule o fatorial de cinco números diferentes de forma assíncrona, onde os cálculos devem ser realizados paralelamente e exiba os resultados conforme forem concluídos, em ordem de menor número para maior número.

import asyncio, math, os
os.system('cls')

numeros = [5, 3, 7, 4, 6]

async def fatorial(fator):
    await asyncio.sleep(fator)
    print(f'Fatorial de {fator} = {math.factorial(fator)}')

async def main():
    tarefa = [asyncio.create_task(fatorial(numero)) for numero in numeros]
    await asyncio.gather(*tarefa)

    
asyncio.run(main())
    




