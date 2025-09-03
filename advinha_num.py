from random import randint

EASY_MODE = 10
HARD_MODE = 5

def verifica_resposta(advinha, resposta, turnos):
    if advinha > resposta:
        print("Numero alto")
        return turnos - 1
    elif advinha < resposta:
        print("Numero baixo")
        return turnos - 1
    else:
        print(f"Voce acertou o numero {resposta}")

def escolha_dificuldade():
    level = input("Escolha uma dificuldade. Escreva 'Facil' ou 'Dificil'")
    if level == "facil":
        return EASY_MODE
    else:
        return HARD_MODE

def jogo():
    print("Seja bem vindo ao advinha numero")
    print("Estou pensando em um numero entre 1 e 100 qual e?")
    resposta = randint(1, 100)
    print(f"A resposta certa e {resposta}")

    turnos = escolha_dificuldade()
    print(f"Voce tem {turnos} tentativas restando")
    adivinha = 0
    while adivinha != resposta:
        adivinha = int(input("Adivinhe um numero: "))
        turnos = verifica_resposta(adivinha, resposta, turnos)
        if turnos == 0:
            print("suas tetativas acabaram. Voce perdeu!")
            return
        elif adivinha != resposta:
            print("Tente de novo!")

jogo()


