import asyncio
import random

jogos = [
    {"id": 1, "times": ("Flamengo", "Palmeiras")},
    {"id": 2, "times": ("São Paulo", "Corinthians")},
    {"id": 3, "times": ("Grêmio", "Internacional")},
]

async def processar_aposta(jogo, futuro):
    tempo = random.randint(2, 8)
    print(f"Aposta no jogo {jogo['id']} ({jogo['times'][0]} vs {jogo['times'][1]}) registrada! Aguardando resultado...\n")

    await asyncio.sleep(tempo)

    resultado = random.choice([f"Vitória do {jogo['times'][0]}", f"Vitória do {jogo['times'][1]}", "Empate"])
    futuro.set_result(resultado)

    print(f"Aposta no jogo {jogo['id']} definida: {resultado} (após {tempo}s).\n")

async def main():
    futuros = [asyncio.Future() for _ in jogos]
    tarefas = [asyncio.create_task(processar_aposta(jogos[i], futuros[i])) for i in range(len(jogos))]

    await asyncio.gather(*tarefas)

    print("Todos os resultados foram revelados!\n")

asyncio.run(main())