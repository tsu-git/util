'''calc_workload.py

    全体予定（OM／標準統計）.xlsxから週ごとの負荷を計算する。
'''
import pandas as pd

# TODO: 引数処理

# TODO: 引数のExcelファイルを読み込む
# TODO: プロジェクト名と担当別の負荷を週ごとに設定したデータを作成
file_path = './全体予定（OM／標準統計）.xlsx'
df = pd.read_excel(file_path, sheet_name='スケジュール_2', engine='openpyxl')

# TODO: NaN値を0に置き換え
df = df.fillna(0)

# TODO: 担当でグループ化し、週ごとの列を合計
df_grouped = df.groupby('担当').sum()
result = df_grouped[df_grouped.index != 0].loc[:, '12/02週':'1/13週']

# TODO: 結果を表示
print(result)
