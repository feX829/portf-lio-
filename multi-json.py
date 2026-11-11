import pandas as pd
import requests
dados = []
pagina = 1

while True:
    url = f"https://quotes.toscrape.com/api/quotes?page={pagina}"
    reponse = requests.get(url)
    dd = reponse.json()
    dados.extend(dd['quotes'])
    if not dd['has_next']:
        break
    pagina += 1
df = pd.DataFrame(dados)
df['autor'] = df['author'].apply(lambda x: x['name'])
df.drop(columns=['author'], inplace=True)
tabela = df.explode('tags')

df.to_csv("teste.csv", index=False)
print(tabela)
