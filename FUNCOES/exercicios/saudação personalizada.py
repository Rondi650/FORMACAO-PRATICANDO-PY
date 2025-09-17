# Beatriz está desenvolvendo um sistema de atendimento para um site de serviços. Ela deseja criar um programa que exiba uma saudação personalizada dependendo da hora do dia que o usuário acessa a plataforma. O sistema deverá ter a seguinte regra:

# Se for antes das 12h, exibir "Bom dia";
# Entre 12h e 18h, exibir "Boa tarde";
# Após 18h, exibir "Boa noite".

def retornar_horario(hora):
    if hora < 12:
        print('Bom dia')
    elif 12 <= hora < 18:
        print('Boa tarde')
    else:
        print('Boa noite')
    
horario = int(input('Digite a hora atual (0-23): '))  
        
if horario <= 23:
    retornar_horario(horario)
else:
    print('Digite um numero entre 0 e 23')
    
