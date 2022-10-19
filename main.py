from functions import limpar_tela, op_invalida, exibe_jogo, mostra_dica, compara_chute, gera_palavra_censurada, exibe_jogo_sem_dica, salva_partida, exibe_historico, jogar_novamente
jogar = True
while jogar:
    nomes = True
    while nomes:
        competidor = input("Insira o nome do competidor: ")
        desafiante = input("Insira o nome do desafiante: ")
        if len(competidor) >= 2 and len(desafiante) >= 2:
            nomes = False
        else: 
            limpar_tela()
            print("Os nomes devem possuir mais de 2 caracteres!")


    limpar_tela()
    
    palavra_chave = input(desafiante + " insira a palavra chave: ")
    
    dica_1 = input(desafiante + " insira a dica número 1: ")
    dica_2 = input(desafiante + " insira a dica número 2: ")
    dica_3 = input(desafiante + " insira a dica número 3: ")
    rodada = True
    limpar_tela()
    vencedor = ""
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
        
        if op == "1":
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
            vencedor = "Desafiante"
        elif palavra_censurada == palavra_chave.upper():
            rodada = False
            print("O Competidor {} venceu!" .format(competidor))
            vencedor = "Competidor"

    salva_partida(desafiante, competidor, palavra_chave, vencedor)
    exibe_historico()
    jogar = jogar_novamente()