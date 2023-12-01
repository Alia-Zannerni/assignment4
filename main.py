from bs4 import BeautifulSoup
import requests

#target url
url='https://coinmarketcap.com/'

#get response from website
result=requests.get(url)

#get web page from the request object using beautifulsoup
doc=BeautifulSoup(result.text,'html.parser')

#get content from the table in the web page
tbody=doc.tbody
trs=tbody.contents

print('--------------------------')

#key value pairs to store coin name and its price
all_prices={}

#saving data of top ten crypto currencies in the dictoinary created above
for tr in trs[:10]:
    name,prixe = tr.contents[2:4]
    coin_name=name.p.string
    coin_price=prixe.span.string
    all_prices[coin_name]=coin_price

print(all_prices)