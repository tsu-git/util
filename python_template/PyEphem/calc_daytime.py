# coding: utf-8
import datetime
import pandas as pd
import ephem

'''
    日の出、日の入り時刻の数列を作成する。
'''

# TODO: 日付のSeriesを作成する
# TODO: 日の出、日の入りのSeriesを作成する
# TODO: 日付のSeriesをインデックスとするDataFrameに日の出、日の入り時間を
#       追加する

if __name__ == "__main__":
    Tokyo = ephem.Observer()

    Tokyo.lat = '35.6810603'
    Tokyo.lon = '139.76730746'
    Tokyo.date = datetime.datetime.now(datetime.UTC)

    sun = ephem.Sun()
    next_sunrise_utc = Tokyo.next_rising(sun)
    next_sunset_utc = Tokyo.next_setting(sun)

    sunrise_local = ephem.localtime(next_sunrise_utc)
    sunset_local = ephem.localtime(next_sunset_utc)

    print(sunrise_local)
    print(sunset_local)
