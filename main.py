from functions import limpar_tela, exibe_jogo, mostra_dica, compara_chute
while True:
    competidor = input("Insira o nome do competidor: ")
    desafiante = input("Insira o nome do desafiante: ")
    limpar_tela()
    
    palavra_chave = input(desafiante + " insira a palavra chave: ")
    
    dica_1 = input(desafiante + " insira a dica número 1: ")
    dica_2 = input(desafiante + " insira a dica número 2: ")
    dica_3 = input(desafiante + " insira a dica número 3: ")
    
    palavra_censurada = exibe_jogo(palavra_chave, dica_1, dica_2, dica_3)
    op = input("Insira uma opção: ")
    dicas = [dica_1, dica_2, dica_3]
    contador_dicas = 0
    if op == "1":
        mostra_dica(dicas, contador_dicas)
        chute = input("Chute uma letra: ")
        palavra_censurada = compara_chute(chute, palavra_chave, palavra_censurada)
        
        