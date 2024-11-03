import pandas as pd
from random import randint, uniform, choice
from datetime import datetime, timedelta

start_dt = datetime.strptime('2024/11/3 00:00:00', '%Y/%m/%d %H:%M:%S')
area_list = ['サンプル市', 'サンプル町', 'サンプル村']
data = [
        {
            'area': f'{choice(area_list)}_{i}',
            'datetime': f'{start_dt + timedelta(minutes=30)*i}',
            'value1': randint(5000, 6000), 
            'value2': round(uniform(200, 2500), 2)
        }
            for i in range(20)]

print(pd.DataFrame(data))
