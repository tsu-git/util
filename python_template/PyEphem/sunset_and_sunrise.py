# coding: utf-8
# %load sunset_and_sunrise.py
import ephem
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MultipleLocator

Tokyo = ephem.Observer()
Tokyo.lat = '35.6810603'
Tokyo.lon = '139.76730746'

sun = ephem.Sun()

def gen_sunrise(sun, observer, date):
    observer.date = date
    sunrise_local = ephem.localtime(observer.previous_rising(sun))
    return sunrise_local
    
def gen_sunset(sun, observer, date):
    observer.date = date
    sunset_local = ephem.localtime(observer.next_setting(sun))
    return sunset_local
    
# 目盛ラベル用フォーマッター
def sec_to_hhmm(x, tick_number):
    h = int(x // 3600)
    m = int((x % 3600) // 60)
    return f"{h:02d}:{m:02d}"

date_list = pd.date_range('2025-01-01', '2026-12-31')

d = {'sun_rise':[gen_sunrise(sun, Tokyo, dt) for dt in date_list],
     'sun_set':[gen_sunset(sun, Tokyo, dt) for dt in date_list]}

df_date = pd.DataFrame(d, index=date_list)
get_ipython().run_line_magic('matplotlib', '')

# time型を秒単位に変換（0:00からの経過時間）
df_date['sun_rise_seconds'] = df_date['sun_rise'].apply(lambda t: t.hour*3600 + t.minute*60 + t.second)
df_date['sun_set_seconds'] = df_date['sun_set'].apply(lambda t: t.hour*3600 + t.minute*60 + t.second)

# グラフ描画
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df_date.index, df_date['sun_rise_seconds'], label='Sunrise', color='orange')
ax.plot(df_date.index, df_date['sun_set_seconds'], label='Sunset', color='blue')

# y軸：1時間（3600秒）間隔でメジャー目盛、30分（1800秒）でマイナー目盛
ax.yaxis.set_major_locator(MultipleLocator(3600))
ax.yaxis.set_minor_locator(MultipleLocator(1800))

# y軸ラベルを HH:MM 形式に
ax.yaxis.set_major_formatter(FuncFormatter(sec_to_hhmm))

# 軸やラベルを調整
ax.set_title('Sunrise and Sunset Time (Tokyo)')
ax.set_ylabel('Time of Day')
ax.set_xlabel('Date')
ax.legend()
ax.grid(which='major', linestyle='-', alpha=0.5)
ax.grid(which='minor', linestyle='--', alpha=0.2)
fig.tight_layout()
