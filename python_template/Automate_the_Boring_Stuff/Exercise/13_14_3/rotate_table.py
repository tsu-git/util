"""rotate_table

    引数のエクセルファイルの行と列を入れ替える
"""

import argparse, openpyxl, sys, logging
from pathlib import Path

# 引数を取得する
parser = argparse.ArgumentParser(
            prog='rotate_table.py',
            description='pivot a table on a Excel worksheet')

parser.add_argument('excel_file', help='Excel file')
parser.add_argument('-d', '--debug', action='store_true',
                    help='print debug log')
args = parser.parse_args()
excel_file = args.excel_file

# ログ出力準備
LOG_FMT = ' %(asctime)s: %(levelname)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=LOG_FMT)
if args.debug is False:
    logging.disable(logging.WARNING)

# 引数のファイルを検査する
p = Path(excel_file)
if p.is_file() is False:
    logging.error(f"{excel_file} is not a file")
    sys.exit()

# 引数のファイルの拡張子を検査する
if p.suffix != '.xlsx':
    logging.error(f"{p.suffix} is not a valid suffix")
    sys.exit()

# 引数のファイル名から新しい名前を生成する
excel_file_new = str(p.parent / p.stem) + "_new" + p.suffix
logging.info(f"generate {excel_file_new}")

# 引数のエクセルファイルを読み込む
try:
    wb = openpyxl.load_workbook(excel_file)
except:
    print(f"Failed to load {excel_file}")
    sys.exit()

sht = wb.active

# 新しいエクセルファイルオブジェクトを生成する
wb_new = openpyxl.Workbook()
sht_new = wb_new.active

# TODO: テーブルを読み込みながら列と行を入れ替える
for i in range(sht.min_row, sht.max_row + 1):
    for j in range(sht.min_column, sht.max_column + 1):
        val = sht.cell(row=i, column=j).value
        sht_new.cell(row=j, column=i).value = val

# TODO: 新しいエクセルファイルに保存する
wb_new.save(excel_file_new)

sys.exit()
