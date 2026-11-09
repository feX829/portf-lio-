import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
GH = []
url = "https://quotes.toscrape.com/"
rq = requests.get(url)
bs = BeautifulSoup(rq.text, "html.parser")
href = bs.find("a", class_="tag")
link_alternativo = urljoin(url, href["href"])
resposta = requests.get(link_alternativo)
bs2 = BeautifulSoup(resposta.text, "html.parser")
citação = bs2.find_all("span", class_="text")
autor = bs2.find_all("small", class_="author")
citação2 = {"ditado": citação, "autor": autor}
GH.append(citação2)
pd1 = pd.DataFrame(citação2)
print(pd1)