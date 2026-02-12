import random
palavras = ["python", "computador", "jogo", "código", "algoritmo", 
            "internet", "programa", "dados", "função", "rede"]

palavra_escolhida = random.choice(palavras)
print(palavra_escolhida)
placeholder = ["_"] * len(palavra_escolhida)
tentativas = len(palavra_escolhida)

while tentativas > 0 and "_" in placeholder:
    print(" ".join(placeholder))  # mostra progresso da palavra
    adivinha = input("Digite uma letra: ")

    if adivinha in palavra_escolhida:
        for i in range(len(palavra_escolhida)):
            if palavra_escolhida[i] == adivinha:
                placeholder[i] = adivinha
    else:
        print("Letra errada!")
        tentativas -= 1

if "_" not in placeholder:
    print("Parabéns! Você adivinhou:", "".join(placeholder))
else:
    print("Acabaram as tentativas! A palavra era:", palavra_escolhida)