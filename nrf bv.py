from bs4 import BeautifulSoup
import requests
import pandas as pd
from tabulate import tabulate
url ="https://store.steampowered.com"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")

titles = soup.find_all('h1')
titles_list = [title.text for title in titles]
df = pd.DataFrame(titles_list, columns=
                  ['Заголовки'])

print(tabulate(df,headers='keys',tablefmt='psql'))
