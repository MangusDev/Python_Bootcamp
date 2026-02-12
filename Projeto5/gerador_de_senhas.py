import random
letras = ['A', 'b', 'C', 'd', 'E', 'f', 'G', 'h', 'I', 'j']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '+']

nr_letras = int(input("Digite quantas letras na senha: \n"))
nr_numeros = int(input("Digite quantos numeros na senha: \n"))
nr_simbolos = int(input("Digite quantos simbolos na senha: \n"))

senha = []

for char in range(0, nr_letras):
    senha.append(random.choice(letras))
for char in range(0, nr_simbolos + 1):
    senha.append(random.choice(simbolos))
for char in range(1, nr_numeros + 1):
    senha.append(random.choice(numeros))

# usar o random.shuffle embaralha as posicoes dos caracteres inseridos na lista, deixando em ordem aleatoria
# na lista, pois o append insere no comeco da lista, sendo assim: priemiro letras, simbolos e numeros
random.shuffle(senha)

print(senha)