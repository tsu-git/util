'''volume_controle.py

    巨大な処理対象のファイルの配置場所やサイズを調整して分割実行できるように
    する。

    30分電力データ仕分けの流れ

        外部スクリプト自動実行ツール
            コマンド生成：
                1. 年月文字列を生成する
                2. 30分電力データ仕分けツールと年月文字列のコマンド組み合
                   わせを生成する 

            コマンド実行：
                3. 生成した年月に対応するファイル名を持つファイル達を一時
                   ディレクトリに移動する
                4. 移動ファイルを解凍する
                    filename.csv.gz -> filename.csv
                5. 移動ファイルのうち、巨大ファイルを分割する
                    分割前ファイルは拡張子名を変更する（例：.csv_orginal）
                6. 一時ディレクトリのcsvファイル一覧を作成する
                7. csvファイル一覧のファイルを一定数（多分4ファイル）ずつ
                   移動前ディレクトリにコピーする
        
                30分電力データ仕分けツール
                    1. 引数の年月からold_30min配下の対象ファイル名を取得し
                       処理を行う。 
                    2. 仕分け後のファイルを30min配下に出力する

                8. 移動前ディレクトリの対象年月ファイルをすべて削除
                9. csvファイル一覧に未処理のファイルがあるか確認
                    ある場合
                        1. 6へ戻る。
                    ない場合
                        1. 一時ディレクトリの分割ファイルを削除する
                        2. 分割前ファイルの拡張子を元に戻す
                        3. 一時ディレクトリのファイルをすべて移動元
                           ディレクトリに戻す（移動する）
                        4. 1へ戻る。 

'''
from pathlib import Path
import doctest

def create_test_csv(filename: str, num_of_lines)-> bool:
    '''create_test_csv()

        テスト用にcsvファイルを生成する

        >>> ret = create_test_csv("./infile.csv", 5)
        >>> print(ret)
        True
        >>> with open("./infile.csv", "r") as f:
        ...     for line in f:
        ...         print(line, end="")
        ...
        line [1]
        line [2]
        line [3]
        line [4]
        line [5]

    '''
    fp = Path(filename)
    with open(fp, "w") as f:
        for num in range(1, num_of_lines+1):
            f.write(f"line [{num}]\n")

    return(True)

def split_file(input_file: str, size: int)-> list:
    '''split_file()

        ファイルを指定サイズに分割する。分割後のファイル名を戻り値として
        返却する。

        >>> in_file = "./infile.csv"
        >>> ret = create_test_csv(in_file, 4)
        >>> print(ret)
        True
        >>> file_list = split_file(in_file, 2)
        >>> print(file_list)
        ['infile_1.csv', 'infile_2.csv']

        >>> ret = create_test_csv(in_file, 5)
        >>> print(ret)
        True
        >>> file_list = split_file(in_file, 2)
        >>> print(file_list)
        ['infile_1.csv', 'infile_2.csv', 'infile_3.csv']


    '''
    file_list = []
    in_file_p = Path(input_file)

    # 入力ファイルの存在チェック
    if not in_file_p.is_file():
        return(file_list)

    # 入力ファイルから拡張子を除去した名前
    path = in_file_p.parent / in_file_p.stem

    # 入力ファイルの拡張子
    suffix = in_file_p.suffix

    # TODO: 出力ファイル名を生成する

    # TODO: ファイルを分割
    num_of_readline = 0
    file_cnt = 0
    with open(in_file_p, "r") as in_f:
        for line in in_f:
            num_of_readline += 1

            if num_of_readline < 2:
                file_cnt += 1
                out_file_p = str(path) + f"_{file_cnt}" + suffix
                file_list.append(out_file_p)
                out_f = open(out_file_p, "w")
            elif num_of_readline > size:
                out_f.close()
                file_cnt += 1
                num_of_readline = 1    # 読込行数のリセット
                out_file_p = str(path) + f"_{file_cnt}" + suffix
                file_list.append(out_file_p)
                out_f = open(out_file_p, "w")

            out_f.write(line)

    out_f.close()

    return(file_list)

# TODO 一定以上大きいファイルを検出する
# TODO 退避ディレクトリを作成する
# TODO ファイルを退避する
# TODO 巨大ファイルを分割する
# TODO 分割済みファイルの一つを元ディレクトリに移動する
# TODO 分割済みファイルの一つを元ディレクトリに移動する
