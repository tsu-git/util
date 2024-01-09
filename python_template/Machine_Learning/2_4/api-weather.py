#!usr/bin/python

import requests
import json
from datetime import datetime

# APIキーの指定
apikey = 'f2d87c95f9dae96d0b2cc79825c93ebe'

# 天気を調べたい都市の一覧
cities = ['Tokyo,JP', 'London,UK', 'New York,US']
# APIのひな型
api = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

# 温度変換（ケルビン -> 摂氏）
k2c = lambda k: k - 273.15

# 各都市の温度を取得する
for name in cities:
    # APIのURLを得る
    url = api.format(city=name, key=apikey)
    # 実際にAPIにリクエストを送信し結果を取得する
    r = requests.get(url)
    r.raise_for_status()
    # 結果はJSON形式なのでコードする
    data = json.loads(r.text)
    # 結果を画面に表示
    print('+ 都市 = ', data['name'])
    print('| 天気 = ', data['weather'][0]['description'])
    print('| 最低気温 = ', k2c(data['main']['temp_min']))
    print('| 最高気温 = ', k2c(data['main']['temp_max']))
    print('| 湿度 = ', data['main']['humidity'])
    print('| 気圧 = ', data['main']['pressure'])
    print('| 気圧 = ', data['main']['pressure'])
    print('| 風速度 = ', data['wind']['speed'])
    print('')
