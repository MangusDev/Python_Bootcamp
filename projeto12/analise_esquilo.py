import pandas as pd

dados = pd.read_csv('esquilo.csv')

total_cinza = len(dados[dados["Primary Fur Color"] == 'Gray'])
total_vermelho = len(dados[dados["Primary Fur Color"] == 'Cinnamon'])
total_preto = len(dados[dados["Primary Fur Color"] == 'Black'])
print(total_cinza)
print(total_vermelho)
print(total_preto)


dicionario_dados = {
    "Cor Principal": ["Cinza", "Vermelho", "Preto"],
    "Qauntidade": [total_cinza, total_vermelho, total_preto ]
}

df = pd.DataFrame(dicionario_dados)

df.to_csv("Total de Cores Principais.csv")