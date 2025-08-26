import art

# TODO 1: Import and Print the Logo
print(art.logo)

# Alfabeto usado
alphabet = list("abcdefghijklmnopqrstuvwxyz")

# Função principal do Cifra de César
def caesar(text, shift, direction):
    output_text = ""

    if direction == "decode":
        shift *= -1

    for letter in text:
        if letter in alphabet:
            # encontra posição da letra
            position = alphabet.index(letter)
            new_position = (position + shift) % len(alphabet)
            output_text += alphabet[new_position]
        else:
            # TODO 2: Manter símbolos, números e espaços
            output_text += letter

    print(f"The {direction}d text is: {output_text}")


# TODO 3: Loop para reiniciar o programa
should_continue = True

while should_continue:
    direction = input("Escreva 'encode' para encriptar, escreva 'decode' to decriptar:\n").lower()
    text = input("Escreva sua Mensagem:\n").lower()
    shift = int(input("Digite quantos numeros de deslocamento:\n"))
    caesar(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")