"""translate_text_to_excel

    テキストファイルからスプレッドシートに変換する。
    1ファイルから読み込む内容は同一列に書き込む。
"""

import openpyxl, argparse, sys, logging
from pathlib import Path

# 引数を取得する
parser = argparse.ArgumentParser(
            prog='translate_text_to_excel',
            description='translate text file(s) to a Excel file')
parser.add_argument('filename', nargs='+')
parser.add_argument('-o', '--outfile', default='out.xlsx')
parser.add_argument('-d', '--debug', action='store_true')
args = parser.parse_args()

# ログ出力の準備をする
FORMAT = '%(asctime)s: %(levelname)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
if args.debug is False:
    logging.disable(level=logging.WARNING)

logging.debug(f"start {sys.argv[0]}")

# 引数のファイルを検査する
for f in args.filename:
    logging.debug(f"input file {f}")
    if Path(f).is_file():
        continue
    logging.error(f"{f} is not a readable file")
    sys.exit(False)

# Excelファイルオブジェクトを生成する
wb = openpyxl.Workbook()
sht = wb.active
excel_filename = args.outfile

# 引数のファイルを順次読み込む
i = 0
for infile in args.filename:
    i += 1
    j = 0
    with open(infile, 'r') as f:
        # ファイルを一行ずつ読み込む
        for line in f:
            # Excelファイルオブジェクトに書き込む
            j += 1
            sht.cell(row=j, column=i).value = line

# Excelファイルオブジェクトを保存する
wb.save(excel_filename)

sys.exit(True)
