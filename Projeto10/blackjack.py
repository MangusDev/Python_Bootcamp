import random

def randomizar():
    jogador = []
    print("Primeira jogada")
    jogador.append(random.randint(1, 10))
    jogador.append(random.randint(1, 10))
    print("Cartas iniciais:", jogador)

    while sum(jogador) < 21:
        jogada = input("Deseja continuar? (s/n): ").lower()
        if jogada == "s":
            nova_carta = random.randint(1, 10)
            jogador.append(nova_carta)
            print("Nova carta:", nova_carta)
            print("Mão atual:", jogador, "→ Total:", sum(jogador))
        elif jogada == "n":
            break
        else:
            print("Entrada inválida. Digite 's' ou 'n'.")
    return jogador

def vencedor(jogador1, jogador2):
    soma1 = sum(jogador1)
    soma2 = sum(jogador2)

    print(f"\nSua mão: {jogador1} → {soma1}")
    print(f"Mão do computador: {jogador2} → {soma2}")

    if soma1 > 21:
        print("Você estourou! O computador venceu.")
    elif soma2 > 21:
        print("O computador estourou! Você venceu.")
    elif soma1 > soma2:
        print("Você venceu!")
    elif soma2 > soma1:
        print("O computador venceu!")
    else:
        print("Empate!")

print("Bem-vindo ao Blackjack!")

jogadas = int(input("Quantas rodadas você quer jogar? "))

for i in range(jogadas):
    print(f"\n Rodada {i+1}")
    print("SUA JOGADA")
    jogador1 = randomizar()
    print("JOGADA DO COMPUTADOR")
    jogador2 = []

    # Simulação simples do computador: para se tiver 17 ou mais
    jogador2.append(random.randint(1, 10))
    jogador2.append(random.randint(1, 10))
    while sum(jogador2) < 17:
        jogador2.append(random.randint(1, 10))

    vencedor(jogador1, jogador2)
