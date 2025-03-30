'''parse_address_str.py

    住所文字列の解析、分割を行う。
'''
import re


def __test_print(*strings, sep="/"):
    '''__test_print()

        doctest用の出力関数。出力が空文字の場合でも、doctestがエラーと
        ならないように出力を[]で囲む。

        >>> __test_print("高知県")
        [高知県]
        >>> __test_print("高知県", "高知市")
        [高知県/高知市]
        >>> __test_print("高知県", "高知市", sep=":")
        [高知県:高知市]
        >>> __test_print("高知県", "高知市", "1", "4")
        [高知県/高知市/1/4]

    '''
    print(f"[{sep.join(strings)}]")

    return


def normalize_address(address_str):
    '''normalize_address()

        住所文字列で使われている数字や区切り文字（列）を揃える
            - 全角ハイフン（複数種類）を半角ハイフンにする
            - 全角スペースを半角スペースにする
            - 全角数字を半角にする
            - 丁目、番地を半角ハイフンにする
            - ハイフン＋数字＋号の「号」を除去する

        >>> address_strs = [
        ...     # 番地号と建物名の間に全角スペースあり、普通の全角ハイフン
        ...     "高知県高知市本町１丁目１−１　サンライズビル３０１号室",
        ...
        ...     # 番地号と建物名の間にスペースなし、異なる全角ハイフンの組
        ...     # み合わせ
        ...     "高知県南国市後免町２－２ー２グリーンハイツＡ棟",
        ...
        ...     # 番地号と建物名の間に全角スペースあり、全角ハイフンを混ぜ
        ...     # た場合
        ...     "高知県四万十市中村一条３―４−５　コスモタワー１００１号室",
        ...
        ...     # 番地号と建物名の間にスペースなし、全角ハイフンの種類を
        ...     # 混ぜた場合
        ...     "高知県安芸市本町４ー６―７さざなみマンション５０２号室",
        ...
        ...     # 番地号と建物名の間に全角スペースあり、全角ハイフンを複数
        ...     # 種類使用
        ...     "高知県須崎市鍋島５－８−９　スプリングパレス２０１号"
        ... ]
        >>> print(normalize_address(address_strs[0]))
        高知県高知市本町1-1-1 サンライズビル301号室
    '''

    # 全角スペースを半角スペースに変換
    address_converted = address_str.replace('　', ' ')

    # 全角ハイフン（例: "ー", "―", "−"）を半角ハイフンに変換
    #   ただし、直前の文字がカタカナに該当しない場合のみ
    #   (?<!...)（否定の先読み）
    address_converted = re.sub(
        r'(?<![ァ-ヶ])[－ー―−]', '-', address_converted)

    # 全角数字を半角に変換
    # TODO: 漢数字の対応を検討する
    address_converted = re.sub(
        r'[０-９]',
        lambda x: chr(ord(x.group(0)) - 0xFEE0),
        address_converted
    )

    # 丁目を半角ハイフンに変換
    address_converted = re.sub(r'丁目', '-', address_converted)
    # 番、番地を半角ハイフンに変換
    address_converted = re.sub(r'(番|番地)', '-', address_converted)
    # ハイフン＋数字＋号の「号」を除去する
    address_converted = re.sub(r'-\d+(号)', '', address_converted)

    return address_converted


def split_address(address_str) -> dict:
    '''split_address()

        引数の住所文字列を住所部分と建物名に分離する。
            - 番地号の後ろに続く建物名を分離する。

        >>> address_strs = [
        ...     # 番地号と建物名の間に全角スペースあり、普通の全角ハイフン
        ...     "高知県高知市本町１丁目１−１　サンライズビル３０１号室",
        ...
        ...     # 番地号と建物名の間にスペースなし、異なる全角ハイフンの組
        ...     # み合わせ
        ...     "高知県南国市後免町２－２ー２グリーンハイツＡ棟",
        ...
        ...     # 番地号と建物名の間に全角スペースあり、全角ハイフンを混ぜ
        ...     # た場合
        ...     "高知県四万十市中村一条３―４−５　コスモタワー１００１号室",
        ...
        ...     # 番地号と建物名の間にスペースなし、全角ハイフンの種類を
        ...     # 混ぜた場合
        ...     "高知県安芸市本町４ー６―７さざなみマンション５０２号室",
        ...
        ...     # 番地号と建物名の間に全角スペースあり、全角ハイフンを複数
        ...     # 種類使用
        ...     "高知県須崎市鍋島５－８−９　スプリングパレス２０１号"
        ... ]
        >>> addr_dict = split_address(address_strs[0])
        >>> print(addr_dict['address'])
        高知県高知市本町1-1-1
        >>> print(addr_dict['building'])
        サンライズビル301号室

        >>> addr_dict = split_address(address_strs[1])
        >>> print(addr_dict['address'])
        高知県南国市後免町2-2-2
        >>> print(addr_dict['building'])
        グリーンハイツＡ棟

        >>> addr_dict = split_address(address_strs[2])
        >>> print(addr_dict['address'])
        高知県四万十市中村一条3-4-5
        >>> print(addr_dict['building'])
        コスモタワー1001号室

        >>> addr_dict = split_address(address_strs[3])
        >>> print(addr_dict['address'])
        高知県安芸市本町4-6-7
        >>> print(addr_dict['building'])
        さざなみマンション502号室

        >>> addr_dict = split_address(address_strs[4])
        >>> print(addr_dict['address'])
        高知県須崎市鍋島5-8-9
        >>> print(addr_dict['building'])
        スプリングパレス201号


            - 丁目、番地号が1つ以上ある場合に対応

        >>> addr_dict = split_address("安芸市本町4-6-7建物名Ａ")
        >>> print(addr_dict['address'])
        安芸市本町4-6-7
        >>> print(addr_dict['building'])
        建物名Ａ

        >>> addr_dict = split_address("安芸市本町4-5建物名Ｂ")
        >>> print(addr_dict['address'])
        安芸市本町4-5
        >>> print(addr_dict['building'])
        建物名Ｂ

        >>> addr_dict = split_address("安芸市本町2建物名Ｃ")
        >>> print(addr_dict['address'])
        安芸市本町2
        >>> print(addr_dict['building'])
        建物名Ｃ

        >>> addr_dict = split_address("安芸市本町4-5-3")
        >>> print(addr_dict['address'])
        安芸市本町4-5-3
        >>> print(f"[{addr_dict['building']}]")
        []

        >>> addr_dict = split_address("安芸市本町3-1")
        >>> print(addr_dict['address'])
        安芸市本町3-1
        >>> print(f"[{addr_dict['building']}]")
        []

        >>> addr_dict = split_address("安芸市本町5")
        >>> print(addr_dict['address'])
        安芸市本町5
        >>> print(f"[{addr_dict['building']}]")
        []

    '''

    # 丁目や番地号の形式にマッチする正規表現
    #   (?:...)非補足グループ：パターンでグループ化するだけで、後で参照
    #   しない。ここでは番地号のパターン（-n-n）を表す。
    pattern = re.compile(r'''
        (.*?                # 住所部分 丁目より前（非貪欲マッチ）
            \d+             # 住所部分 丁目
            (?:-\d+){0,2})  # 住所部分 番地号（あれば）
        (.*)                # 建物部分
        ''', re.VERBOSE)
    match = re.match(pattern, normalize_address(address_str))

    # ディクショナリ形式で返却する
    if match:
        return {
            # 住所部分
            'address': match.group(1).strip(),
            # 建物部分（存在しない場合は空文字列）
            'building': match.group(2).strip()
        }
    else:
        return {
            # マッチしない場合はそのまま
            'address': address_str.strip(),
            'building': ''
        }


def parse_chome_and_banchi(address_str) -> dict:
    '''parse_chome_and_banch()

        丁目番地号を分割する。
        文字列は次の関数により処理されている前提
            - split_address()で建物名が分離されている

        >>> address_without_bld_name = "安芸市本町4-6-7"
        >>> addr_dict = ""
        >>> addr_dict = parse_chome_and_banchi(address_without_bld_name)
        >>> __test_print(addr_dict['location_base'])
        [安芸市本町]
        >>> __test_print(addr_dict['chome'], addr_dict['banchi'],
        ...             addr_dict['gou'])
        [4/6/7]

        >>> address_without_bld_name = "高知県四万十市中村一条3-4"
        >>> addr_dict = ""
        >>> addr_dict = parse_chome_and_banchi(address_without_bld_name)
        >>> __test_print(addr_dict['location_base'])
        [高知県四万十市中村一条]
        >>> __test_print(addr_dict['chome'], addr_dict['banchi'],
        ...             addr_dict['gou'])
        [3/4/]

        >>> address_without_bld_name = "高知県四万十市中村一条3"
        >>> addr_dict = ""
        >>> addr_dict = parse_chome_and_banchi(address_without_bld_name)
        >>> __test_print(addr_dict['location_base'])
        [高知県四万十市中村一条]
        >>> __test_print(addr_dict['chome'], addr_dict['banchi'],
        ...             addr_dict['gou'])
        [3//]

    '''

    # TODO: 住所の各要素を分解して格納する（実装中）

    # 丁目や番地号の形式にマッチする正規表現
    #   (?:...)非補足グループ：パターンでグループ化するだけで、後で参照
    #   しない。ここでは番地号のパターン（-n-n）を表す。
    pattern = re.compile(r'''
        (.*?)               # 住所部分 丁目より前（非貪欲マッチ）
            (\d+            # 住所部分 丁目
            (-\d+){0,2})    # 住所部分 番地号（あれば）
        ''', re.VERBOSE)

    match = re.match(pattern, address_str)
    chome_banchi_gou = match.group(2).strip().split('-')

    address_splited = dict(location_base="", chome="", banchi="", gou="")
    address_splited['location_base'] = match.group(1).strip()
    if len(chome_banchi_gou) > 0:
        address_splited['chome'] = chome_banchi_gou[0]
    if len(chome_banchi_gou) > 1:
        address_splited['banchi'] = chome_banchi_gou[1]
    if len(chome_banchi_gou) > 2:
        address_splited['gou'] = chome_banchi_gou[2]

    return address_splited


def remove_extra_after_prefix():
    '''remove_extra_after_prefix

        指定された住所文字列（prefix）より後ろの余計な部分を削除する
    '''

    return
