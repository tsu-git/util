"""upd_delivery_list.py
    納品一覧の項目のいくつかを、手入力値に基づいて計算する

        対応済みの項目
        - カラム区分

"""
def search

import sys
from pathlib import Path
import openpyxl

# 引数取得
if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} delivery_list_file.xlsx")
    sys.exit()

list_file = Path(sys.argv[1])
if list_file.is_file() != True:
    print(f"{list_file} dose not exist")
    print(f"Usage: {sys.argv[0]} delivery_list_file.xlsx")
    sys.exit()

if list_file.suffix != ".xlsx":
    print(f"{list_file} is not a excel file")
    print(f"Usage: {sys.argv[0]} delivery_list_file.xlsx")
    sys.exit()


# 納品一覧ファイルを開く
wb = openpyxl.load_workbook(list_file)

# 対象のシートを選択する
sheet = wb['Sheet1']

# TODO: ヘッダ行を探す

# TODO: ファイル名から項目を自動計算する

# TODO: 納品一覧ファイルを保存

# TODO: 納品一覧ファイルを閉じる

sys.exit()
