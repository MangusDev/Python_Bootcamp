
print("Seja bem vindo a ilha do Tesouro")
print("Sua missao e encontrar o tessouro, voce tem 3 tentativas")
tentativas = 3
while tentativas != 0:
    escolha1 = input("Voce esta saindo de uma caverna. Escolha um lado: direita ou esquerda: ")
    if escolha1 == "esquerda":
        escolha2 = input("Voce chegou na beira de um lago. Escolha: esperar barco ou nadar: ")
        if escolha2 == "esperar":
            escolha3 = input("Voce chegou na ilha, tem uma casa com 3 portar, qual cor voce escolhe: Azul, Vermelho ou Verde:  ")
            if escolha3 == "vermelho":
                print("Escolheu a porta errada e um monstro te pegou =( ")
                tentativas -= 1
                if tentativas == 0:
                    break
            elif escolha3 == "azul":
                print("Escolheu a porta errada e caiu no calabouso =( ")
                tentativas -= 1
                if tentativas == 0:
                    break
            else:
                print("Voce encontrou o tesouro!!!!")
                print('''
*******************************************************************************
|                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
                break
        else:
            print("Escolheu o caminho errado afundou no lago =( ")
            tentativas -= 1
            if tentativas == 0:
                break
    else:
        print("Escolheu o lado errado caiu em um buraco =( ")
        tentativas -= 1
        if tentativas == 0:
                break
