import random
papel = '''
                     _.-._
                    | | | |_
                    | | | | |
                    | | | | |
                  _ |  '-._ |
                  \`\`-.'-._;
                   \    '   |
                    \  .`  /
                     |    |
'''
pedra = '''
                               _
              _        ,-.    / )
             ( `.     // /-._/ /
              `\ \   /(_/ / / /
                ; `-`  (_/ / /
                |       (_/ /
                \          /
                 )       /`
                /      /`
'''

tesoura = '''
                       _
                         / )
                        / /    _
              _        / /    / )
             ( `.     / /-.  / /
              `\ \   / // /`/ /
                ; `-`  (_/ / /
                |       (_/ /
                \          /
                 )       /`
                /      /`
'''
jogadas = [pedra, papel, tesoura]

usuario = int(input("Escolha pedra (0), papel (1) ou tesoura (2): "))
computador = random.randint(0, 2)

print(f"\nVocê escolheu:\n{jogadas[usuario]}")
print(f"Computador escolheu:\n{jogadas[computador]}")

# Lógica do jogo
if usuario == computador:
    print("Empate!")
elif (usuario == 0 and computador == 2) or \
     (usuario == 1 and computador == 0) or \
     (usuario == 2 and computador == 1):
    print("Você ganhou!!! 🎉")
else:
    print("Computador ganhou 😢")

