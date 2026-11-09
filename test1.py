import pandas as pd
import requests
url = "https://quotes.toscrape.com/api/quotes?page=1"
response = requests.get(url)
dados = response.json()
df = pd.DataFrame(dados['quotes'])
    
df['autor'] = df['author'].apply(lambda x: x['name'])