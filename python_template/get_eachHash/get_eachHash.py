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
    print(f"{directory} is not found")
    sys.exit(1)

# デフォルトの出力ファイル名を生成
if not outfile:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    outfile = f"hash_list_{timestamp}.txt"

# 出力ファイルが存在しない場合は作成
if not os.path.isfile(outfile):
    open(outfile, 'w').close()

# ファイルリストを取得
file_list = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
num_of_files = len(file_list)
print(f"Got {num_of_files} files from {directory}")

# ハッシュ値取得
with open(outfile, 'a', encoding='utf-8') as o_file:
    for file_name in file_list:
        file_path = os.path.join(directory, file_name)
        with open(file_path, 'rb') as file:
            bytes = file.read()  # ファイル内容を読み込む
            file_hash = hashlib.sha256(bytes).hexdigest()  # SHA256ハッシュ値を計算
            o_file.write(f"{file_name} {file_hash}\n")

print(f"{sys.argv[0]} finished to output file hashes: ")
print(os.path.abspath(outfile))
