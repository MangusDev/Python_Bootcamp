print("Bem vindo a calculadora")

def calculadora(a, b, operacao):
    resultado = 0
    if operacao == "+":
        resultado = (a + b)
    elif operacao == "-":
        resultado = (a - b)
    elif operacao == "*":
        resultado = (a * b)
    else:
        resultado = (a / b)
    return resultado

a = float(input("digite o primeiro numero: "))
operacao = input("escola a operacao: + " 
    " - " 
    " * " 
    " / ")
b = float(input("digite o segundo numero: "))

resultado = calculadora(a, b, operacao)

print(resultado)


