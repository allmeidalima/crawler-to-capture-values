from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import pandas as pd
import re

html = urlopen('https://www.lidl.co.uk/food-offers')
soup = bs(html, 'html.parser')
product_names = soup.find_all('h3', {'class': 'ret-o-card__headline'})
product_prices = soup.find_all('span', {'class' : 'lidl-m-pricebox__price'})

products = []
prices = []

for n in range(len(product_names)):
    clean_name_product = re.sub("\\xa0|\\n|2|", " ", product_names[n].text)
    products.append(clean_name_product)

for p in range(len(product_prices)): 
    prices.append(product_prices[p].text)

df = pd.DataFrame({'Produtos': products , 'Valores': prices})
print(df)
