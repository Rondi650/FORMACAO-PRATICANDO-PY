import time

'''MODO SINCRONO'''
def tarefa(numero):
    print(f'Iniciando tarefa {numero}')
    time.sleep(2)
    print(f'Tarefa {numero} concluida!')
    
tarefa(1)
tarefa(2)
tarefa(3)





