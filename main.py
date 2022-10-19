from functions import limpar_tela, op_invalida, exibe_jogo, mostra_dica, compara_chute, gera_palavra_censurada, exibe_jogo_sem_dica
while True:
    competidor = input("Insira o nome do competidor: ")
    desafiante = input("Insira o nome do desafiante: ")
    limpar_tela()
    
    palavra_chave = input(desafiante + " insira a palavra chave: ")
    
    dica_1 = input(desafiante + " insira a dica número 1: ")
    dica_2 = input(desafiante + " insira a dica número 2: ")
    dica_3 = input(desafiante + " insira a dica número 3: ")
    rodada = True
    limpar_tela()
    
    palavra_censurada = gera_palavra_censurada(palavra_chave)

    dicas = [dica_1, dica_2, dica_3]
    contador_dicas = 0
    erros = 0
    
    while (rodada):
        if contador_dicas < 3:
            exibe_jogo(palavra_chave, dica_1, dica_2, dica_3, palavra_censurada, erros)
            op = input("Insira uma opção: ")        
        else:
            exibe_jogo_sem_dica(palavra_chave, palavra_censurada, erros)
            op = "2"

        if op == "1": #Só pode ser chamada 3 vezes, tem que ajeitar quando finalizar o code
            contador_dicas = mostra_dica(dicas, contador_dicas)
            chute = input("Chute uma letra: ")
            comparacao = compara_chute(chute, palavra_chave, palavra_censurada, erros)
            palavra_censurada = comparacao[0]
            erros = comparacao[1]
        elif op == "2":
            chute = input("Chute uma letra: ")
            comparacao = compara_chute(chute, palavra_chave, palavra_censurada, erros)
            palavra_censurada = comparacao[0]
            erros = comparacao[1]
        else:
            op_invalida()
            continue

        if erros == 5:
            rodada = False
            print("O Desafiante {} venceu!" .format(desafiante))
        elif palavra_censurada == palavra_chave.upper():
            rodada = False
            print("O Competidor {} venceu!" .format(competidor))

        