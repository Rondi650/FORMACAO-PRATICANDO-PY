import os
os.system('cls')

def limpar_texto(texto_digitado):
    texto_digitado = texto_digitado.strip().lower()
    caracteres =  ",.!|?;:\"'_-()[]{}#"
    for char in caracteres:
        texto_digitado = texto_digitado.replace(char,'')
    return texto_digitado
        
def contar_palavras(frase):
    frase = limpar_texto(frase).split()
    if not frase:
        return {}
    else:
        palavras = {}
        for palavra in frase:
                palavras[palavra] = palavras.get(palavra,0) +1
        return palavras
        
texto = input('Digite o texto para a contagem de palavras: ') # Python python é bom!
if not texto:
    print('Digite uma frase')
else:
    resultado = contar_palavras(texto)
    for chave, valor in resultado.items():
        print(f'{chave} - {valor}')
        
        