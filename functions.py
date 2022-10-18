import os
def limpar_tela(): 
    os.system("cls")

def exibe_jogo(palavra_chave, dica_1, dica_2, dica_3):
    limpar_tela()
    numero_caracteres = len(palavra_chave)
    palavra_censurada = ""
    dicas = [dica_1, dica_2, dica_3]
    contador = 0
    for index in range(0, numero_caracteres): 
        palavra_censurada += "*"
    print("A palavra chave possuí {} letras." .format(numero_caracteres))
    print(palavra_censurada)
    print("Receber Dica (1)")
    print("Adivinhar Letra(2)")
    return palavra_censurada
        
def mostra_dica(dicas, contador):
    print(dicas[contador])
    contador+=1
    return contador

def compara_chute(chute, palavra_chave, palavra_censurada): 
    chute = chute.upper()
    palavra_chave = palavra_chave.upper()
    indice = 0 
    palavra_censurada_nova = []
    
    for letra in palavra_chave:
        if chute == letra:
            palavra_censurada_nova.append(letra)
            continue
        else:
            palavra_censurada_nova.append("*")
            continue
    return(''.join(palavra_censurada_nova))