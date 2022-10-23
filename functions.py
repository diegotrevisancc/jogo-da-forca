import os
import time


def limpar_tela():
    os.system("cls")


def configura_jogo(desafiante):
    try:
        palavra_chave = input(desafiante + " insira a palavra chave: ")
        dica_1 = input(desafiante + " insira a dica número 1: ")
        dica_2 = input(desafiante + " insira a dica número 2: ")
        dica_3 = input(desafiante + " insira a dica número 3: ")
        retorno = [palavra_chave, dica_1, dica_2, dica_3]
    except:
        print("Insira valores válidos!")
    return retorno


def gera_palavra_censurada(palavra_chave):
    palavra_censurada = ""
    numero_caracteres = len(palavra_chave)
    for index in range(0, numero_caracteres):
        palavra_censurada += "*"
    return palavra_censurada


def exibe_jogo(palavra_chave, dica_1, dica_2, dica_3, palavra_censurada, erros):
    dicas = [dica_1, dica_2, dica_3]
    contador = 0
    limpar_tela()
    print("A palavra chave possuí {} letras." .format(len(palavra_chave)))
    exibe_palavra_erros(palavra_censurada, erros)
    print("Receber Dica (1)")
    print("Adivinhar Letra(2)")
    print('---------------------\n')


def exibe_jogo_sem_dica(palavra_chave, palavra_censurada, erros):
    limpar_tela()
    print("A palavra chave possuí {} letras." .format(len(palavra_chave)))
    exibe_palavra_erros(palavra_censurada, erros)


def mostra_dica(dicas, contador):
    print(dicas[contador])
    contador += 1
    return contador


def compara_chute(chute, palavra_chave, palavra_censurada, erros):
    chute = chute.upper()
    palavra_chave = palavra_chave.upper()
    palavra_censurada_nova = list(palavra_censurada)
    acertou = False
    for index in range(0, len(palavra_chave)):
        if chute == palavra_censurada[index]:
            limpar_tela()
            print("Você já chutou essa letra!")
            time.sleep(0.15)
            break
        if palavra_chave[index] == chute:
            palavra_censurada_nova[index] = chute
            acertou = True
        else:
            continue

    if acertou == False:
        erros += 1
        limpar_tela()
        erro()
    else:
        limpar_tela()
        acerto()
        pass

    retorno = [(''.join(palavra_censurada_nova)), erros]
    return retorno


def op_invalida():
    limpar_tela()
    print("Opção Inválida")
    print("Por favor, selecione a opção 1 ou a opção 2")
    time.sleep(2.5)


def exibe_palavra_erros(palavra_censurada, erros):
    print(palavra_censurada)
    print("Erros: " + str(erros))
    print('---------------------\n')


def acerto():
    acertou = "ACERTOU!"
    for letra in acertou:
        print(letra)
        time.sleep(0.10)


def erro():
    errou = "ERROU!"
    for letra in errou:
        print(letra)
        time.sleep(0.10)


def salva_partida(desafiante, competidor, palavra_chave, vencedor):
    file = open("historico.txt", "r")
    partidas_anteriores = file.readlines()
    file.close()
    file = open("historico.txt", "w")
    for item in partidas_anteriores:
        file.write(item)
    if vencedor == "Desafiante":
        file.write("Palavra Chave: " + palavra_chave + " - Vencedor: Desafiante " +
                   desafiante + ", Perdedor: Competidor: " + competidor + "\n")
    else:
        file.write("Palavra Chave: " + palavra_chave + " - Vencedor: Competidor " +
                   competidor + ", Perdedor: Desafiante: " + desafiante + "\n")
    file.close()


def exibe_historico():
    file = open("historico.txt", "r")
    conteudo = file.read()
    print(conteudo)
    file.close()


def jogar_novamente():
    while True:
        try:
            while True:
                jogar = int(input("Deseja jogar novamente? Sim(1) Não(2): "))
                if jogar == 1:
                    jogar = True
                    return jogar
                    break
                elif jogar == 2:
                    jogar = False
                    return jogar
                    break
                else:
                    print("Insira apenas 1 ou 2!")
        except:
            print("Insira um número!")
        jogar = int(input("Escolha apenas 1 ou 2: "))
