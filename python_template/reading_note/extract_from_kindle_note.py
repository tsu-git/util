from bs4 import BeautifulSoup
import sys

"""extract_from_kindle_note

    Kindleノートからダウンロードした「メモとハイライト」ページから読書ノート
    向けに必要な情報を抽出
"""

# 引数からダウンロードファイルのパスを取得
if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} filename")
    sys.exit()
file = sys.argv[1]
print(f"extract from {file}")

# ダウンロードファイルを開く
with open(file, "r") as f:
    # ダウンロードファイルを解析 
    soup = BeautifulSoup(f, "html.parser")


# 抽出した内容を出力
title = soup.select_one('#annotation-scroller > div > div.a-row.a-spacing-base > div.a-column.a-span5 > h3').string
auther = soup.select_one('#annotation-scroller > div > div.a-row.a-spacing-base > div.a-column.a-span5 > p.a-spacing-none.a-spacing-top-micro.a-size-base.a-color-secondary.kp-notebook-selectable.kp-notebook-metadata').string
print(f"{title}: {auther}")

print("-" * 3)
print("メモとハイライト", end="\n\n")
highlite_list = soup.select('#highlight')
note_list = soup.select('#note')
for i, highlite in enumerate(highlite_list):
    print(f"{i+1}. {highlite.string}", end="\n")
    if note_list[i].string:
        print(f"    note: {note_list[i].string}", end="\n\n")
    else:
        print()

sys.exit()
