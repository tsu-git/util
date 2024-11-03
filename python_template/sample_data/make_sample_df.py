import pandas as pd
from random import randint, uniform, choice

# coding: utf-8
area_list = ['サンプル市', 'サンプル町', 'サンプル村']
data = [{'area': f'{choice(area_list)}_{i}',
         'value1': randint(5000, 6000), 
         'value2': round(uniform(200, 2500), 2)}
            for i in range(20)]

print(pd.DataFrame(data))
