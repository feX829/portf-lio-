from bs4 import BeautifulSoup
import requests
import pandas as pd
tabela = []
url = "https://quotes.toscrape.com/"
acesso = requests.get(url)
dados = BeautifulSoup(acesso.text, "html.parser")
dd = dados.find_all("div", class_="quote")
for citacoes in dd:
    texto = citacoes.find("span", class_="text").text
    autor = citacoes.find("small", class_="author").text
    lists = {
            "citacao": citacoes,
            "autor": autor
            }
    tabela.append(lists)




    print(autor)
df = pd.DataFrame(tabela)
print(df)
