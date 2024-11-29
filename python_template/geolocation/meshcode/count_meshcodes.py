# coding: utf-8
file_list = list(p.glob('[0-9][0-9].csv'))
df = pd.concat([pd.read_csv(file, encoding="sjis", dtype='object') for file in file_list])
df['pref_code'] = df['都道府県市区町村コード'].str[:2]
df.groupby('pref_code')['基準メッシュ・コード'].count()
