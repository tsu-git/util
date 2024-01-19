from bs4 import BeautifulSoup
import urllib.request as req

# HTMLを取得
url = "https://finance.yahoo.co.jp/quote/USDJPY=X"
res = req.urlopen(url)

# HTMLを解析
soup = BeautifulSoup(res, "html.parser")

# 任意のデータを抽出
price = soup.select_one("#contents > div > div._1ziqiIUl > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div._1-HjOuwn > div._103wsUl4 > div._2AQd5-ZG > p._1c9rs8VH > span").string
print("usd/jpy=", price)
