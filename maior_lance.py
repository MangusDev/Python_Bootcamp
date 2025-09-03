print("Maior lance!!!")
def recebe_lances(lances):
    mais_lances = True
    while mais_lances:
        name = input("Digite seu nome: ")
        lance = int(input("Digite seu lance R$ "))
        lances[name] = lance

        continuar = input("Deseja fazer mais lances? (s/n)")

        if continuar == "n":
            mais_lances = False

def encontrar_maior_lance(lances):
    maior_lance = 0
    vencedor = ""
    for name in lances:
        lance = lances[name]
        if lance > maior_lance:
            maior_lance = lance
            vencedor = name
            print(f"O vencedor foi: {vencedor}!!, com o lance de: R${maior_lance}")

print("Lances registrados")

lances = {}
recebe_lances(lances)
encontrar_maior_lance(lances)
