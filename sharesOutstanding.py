import requests
from bs4 import BeautifulSoup

#Beta
url = f'https://www.marketwatch.com/investing/stock/aapl?mod=search_symbol'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')
b = soup.findAll('li', class_="kv__item")[6]
b = float(b.text[5:].strip())


#Shares outstanding
url = f'https://www.marketwatch.com/investing/stock/aapl?mod=search_symbol'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')
so = soup.findAll('li', class_="kv__item")[4]
so = so.text[20:].strip()
if 'M' in so:
    so = float(so[:-1]) * 1000000
elif 'B' in so:
    so = float(so[:-1]) * 1000000000


#Operating cash flow
url = 'https://www.marketwatch.com/investing/stock/aapl/financials/cash-flow'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')
cash = soup.findAll('div', class_="cell__content")




#Cash per share
#Debt per share

