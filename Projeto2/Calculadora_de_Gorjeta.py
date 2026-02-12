print("Seja bem vindo a calculadora de gorjeta!")
conta = float(input("Valor da conta: "))
gorjeta = float(input("Quanto voce quer dar de gorjeta? 10 12 15"))
pessoas = float(input("quantas pessoas voce quer divir? "))

if gorjeta not in [10, 12, 15]:
    print("gorjeta deve ser 10, 12 ou 15? ")
else:
    conta_com_gorjeta = conta + (conta * gorjeta/100)
    valor_por_pessoa = conta_com_gorjeta / pessoas
    print(f"Valor da conta com gorjeta R$:{conta_com_gorjeta:.2f}")
    print(f"Cada pessoa deve Pagar: R${valor_por_pessoa:.2f}")
