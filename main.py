
import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

#res = requests.get("http://search.books.com.tw/search/query/key/python/cat/all")
res = requests.get("http://www.marketwatch.com/investing/stock/aapl")
#logger.debug("res = {}".format(res.text))

from bs4 import BeautifulSoup
soup = BeautifulSoup(res.text,'html.parser')
#logger.debug("soup = {}".format(soup.title.string))

#logger.debug("div = {}".format(soup.select("div[class='content-region']")))
#logger.debug("h2 = {}".format(soup.select("h2[class='title']")))    #Get data with tag h2
#logger.debug("span = {}".format(soup.select("span[class='kv__value']")))

#logger.debug("h2 = {}".format(soup.select("h2[class='title']")))

kv__labels = pd.Series()
for kv__label in soup.select("small[class='kv__label']"):
    kv__labels = kv__labels.append(pd.Series([kv__label.contents])).reset_index(drop=True)
#logger.debug("kv__labels = {}".format(kv__labels))

kv__values = pd.Series()
for kv__value in soup.select('span[class="kv__value kv__primary "]'):
    kv__values = kv__values.append(pd.Series([kv__value.contents])).reset_index(drop=True)

df = pd.DataFrame({'Value': kv__values, 'Label': kv__labels})
logger.debug("df = {}".format(df[['Label', 'Value']]))
