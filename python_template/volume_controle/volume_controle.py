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
                4. 移動ファイルのうち、巨大ファイルを分割する
                    分割前ファイルは拡張子名を変更する（例：.csv_orginal）
                5. 一時ディレクトリのcsvファイル一覧を作成する
                6. csvファイル一覧のファイルを一定数（多分4ファイル）ずつ
                   移動前ディレクトリにコピーする
        
                30分電力データ仕分けツール
                    1. 引数の年月からold_30min配下の対象ファイル名を取得し
                       処理を行う。 
                    2. 仕分け後のファイルを30min配下に出力する

                7. 移動前ディレクトリの対象年月ファイルをすべて削除
                8. csvファイル一覧に未処理のファイルがあるか確認
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

def split_file(input_file: str, size: int)-> list:
    '''split_file()

        ファイルを指定サイズに分割する。分割後のファイル名を戻り値として
        返却する。

        >>> in_file = "./in_file.csv"
        >>> with open(in_file, "w") as f:
        >>>     for num in range(1, 3):
        >>>         f.write(f"line [{num:3}]\n")
        >>>
        >>> file_list = split_file(in_file, 10)
        >>> print(f"{len(file_list)}")
        10

    '''
    file_list = []

    in_file_p = Path(input_file)

    # 入力ファイルの存在チェック
    if not in_file_p.is_file():
        return(file_list)

    # 入力ファイルから拡張子を除去した名前
    path = in_file_p.parent / in_file_p.stem
    suffix = in_file_p.suffix

    # TODO: 出力ファイル名を生成する

    # TODO: ファイルを分割
    line_num
    file_cnt = 0
    with open(in_file_p, "r") as in_f:
        for line in in_f:
            if line_num <= size:
                continue
            else:
                line_num = 0
                file_cnt += 1
                out_file_p = path / "_{file_cnt}" / suffix
                file_list.append(out_file_p)

    return(file_list)

# TODO 一定以上大きいファイルを検出する
# TODO 退避ディレクトリを作成する
# TODO ファイルを退避する
# TODO 巨大ファイルを分割する
# TODO 分割済みファイルの一つを元ディレクトリに移動する
# TODO 分割済みファイルの一つを元ディレクトリに移動する
