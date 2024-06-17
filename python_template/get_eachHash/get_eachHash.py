import hashlib
import os
import sys
from datetime import datetime

# 引数チェック
if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} directory [outfile]")
    sys.exit(1)

directory = sys.argv[1]
outfile = sys.argv[2] if len(sys.argv) > 2 else ""

# ディレクトリ存在チェック
if not os.path.isdir(directory):
    print(f"Error: The first argument must be a directory.")
    sys.exit(1)

# デフォルトの出力ファイル名を生成
if not outfile:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    outfile = f"hash_list_{timestamp}.txt"

# 出力ファイルが存在しない場合は作成
if not os.path.isfile(outfile):
    open(outfile, 'w').close()

# ハッシュ値取得と出力
def get_hashes_recursive(dir_path, out_file):
    out_file.write(f"{dir_path}\n")  # ディレクトリを出力ファイルの最初の行に出力
    for root, dirs, files in os.walk(dir_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            with open(file_path, 'rb') as file:
                bytes = file.read()  # ファイル内容を読み込む
                file_hash = hashlib.sha256(bytes).hexdigest()  # SHA256ハッシュ値を計算
                out_file.write(f"{file_name} {file_hash}\n")  # ファイル名とハッシュ値を出力

# ファイルリストを取得してハッシュ値を計算
with open(outfile, 'a', encoding='utf-8') as o_file:
    get_hashes_recursive(directory, o_file)

print(f"{sys.argv[0]} finished to output file hashes: ")
print(os.path.abspath(outfile))

