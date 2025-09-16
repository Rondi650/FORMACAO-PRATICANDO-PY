# Fernanda está planejando uma viagem e quer calcular quanto pagará de pedágio. O valor do pedágio depende da distância percorrida:

# Até 100 km: R$ 10,00
# Entre 100 km e 200 km: R$ 20,00
# Acima de 200 km: R$ 30,00

# Crie um programa que receba a distância percorrida e informe o valor do pedágio correspondente.

distancia = float(input('Digite a distancia percorrida (em km): '))
pedagio_minimo = 10
pedagio_medio = 20
pedagio_maximo = 30

if distancia <= 100:
    print(f'Valor do pedagio: R${pedagio_minimo}')
elif 100 < distancia <= 200:
    print(f'Valor do pedagio: R${pedagio_medio}')
else:
    print(f'Valor do pedagio: R${pedagio_maximo}')