# Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar suas despesas. O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.

limite = 3000
despesas = float(input('Digite o total de despesas do mes (R$): '))

if despesas > limite:
    print('Atencao! Voce ultrapassou o limite do orcamento')
else:
    print('Dentro do limite de orcamento')