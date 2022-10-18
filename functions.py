import os
def limpar_tela(): 
    os.system("cls")

def gera_palavra_censurada(palavra_chave): 
    palavra_censurada = ""
    numero_caracteres = len(palavra_chave)
    for index in range(0, numero_caracteres): 
        palavra_censurada += "*"
    return palavra_censurada
def exibe_jogo(palavra_chave, dica_1, dica_2, dica_3, palavra_censurada):
    dicas = [dica_1, dica_2, dica_3]
    contador = 0
    print("A palavra chave possuí {} letras." .format(len(palavra_chave)))
    print(palavra_censurada)
    print("Receber Dica (1)")
    print("Adivinhar Letra(2)")
    print('---------------------\n')
        
def mostra_dica(dicas, contador):
    print(dicas[contador])
    contador+=1
    return contador

def compara_chute(chute, palavra_chave, palavra_censurada, erros): 
    chute = chute.upper()
    palavra_chave = palavra_chave.upper()
    indice = 0 
    palavra_censurada_nova = list(palavra_censurada)
    acertou = False
    for index in range(0, len(palavra_chave)):
        if palavra_chave[index] == chute:
            palavra_censurada_nova[index] = chute
            acertou = True
        else:
            continue

    if acertou == False:
        erros+=1
    else:
        pass

    retorno = [(''.join(palavra_censurada_nova)), erros]
    return retorno