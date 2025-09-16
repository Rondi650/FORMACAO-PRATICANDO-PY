# Uma professora precisa de um programa que ajude a calcular a média final dos alunos e informe se foram aprovados, ficaram de recuperação ou reprovados. As regras são:

# Média >= 7: Aprovado
# 5 <= Média < 7: Recuperação
# Média < 5: Reprovado

# Escreva um programa que receba três notas como entrada e calcule a média final. Com base na média, exiba a situação do aluno.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

lista = [nota1,nota2,nota3]
soma = sum(lista)
qtd = len(lista)
media = (soma/qtd)

if media >=7:
    print(f'Media {media:.2f}, Aprovado.')
elif 5 <= media <= 7:
    print(f'Media {media:.2f}, Recuperacao.')
else:
    print(f'Media {media:.2f}, Reprovado.')

