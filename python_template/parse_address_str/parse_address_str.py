'''parse_address_str.py

    住所文字列の解析、分割を行う。
'''
import re, shelve
from pathlib import Path


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
        ...     "高知県須崎市鍋島５－８−９　スプリングパレス２０１号",
        ...
        ...     # 丁目番地号
        ...     "高知県須崎市鍋島５丁目８番地９号　スプリングパレス２０１号",
        ...
        ...     # 番地号
        ...     "広島県尾道市西藤町字合六１７９番１１",
        ...
        ...     # 番地
        ...     "広島県尾道市西藤町字合六１７９番",
        ...
        ...     # 建物名に「番」
        ...     "広島県尾道市西藤町字合六１７９番１１パレス２番館"
        ... ]
        >>> print(normalize_address(address_strs[0]))
        高知県高知市本町1-1-1 サンライズビル301号室

        >>> print(normalize_address(address_strs[5]))
        高知県須崎市鍋島5-8-9 スプリングパレス201号

        >>> print(normalize_address(address_strs[6]))
        広島県尾道市西藤町字合六179-11

        >>> print(normalize_address(address_strs[7]))
        広島県尾道市西藤町字合六179

        >>> print(normalize_address(address_strs[8]))
        広島県尾道市西藤町字合六179-11パレス2番館
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
    address_converted = re.sub(r'(-?\d+)番地(\d)', r'\1-\2', address_converted)
    address_converted = re.sub(r'(-?\d+)番(\d)', r'\1-\2', address_converted)
    # 番、番地で終わる場合は「番」「番地」を除去する
    address_converted = re.sub(r'(-?\d+)番地$', r'\1', address_converted)
    address_converted = re.sub(r'(-?\d+)番$', r'\1', address_converted)
    # ハイフン＋数字＋号の「号」を除去する
    address_converted = re.sub(r'(-\d+)号', r'\1', address_converted)

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
        >>> __test_print(addr_dict['address'])
        [高知県高知市本町1-1-1]
        >>> __test_print(addr_dict['building'])
        [サンライズビル301号室]

        >>> addr_dict = split_address(address_strs[1])
        >>> __test_print(addr_dict['address'])
        [高知県南国市後免町2-2-2]
        >>> __test_print(addr_dict['building'])
        [グリーンハイツＡ棟]

        >>> addr_dict = split_address(address_strs[2])
        >>> __test_print(addr_dict['address'])
        [高知県四万十市中村一条3-4-5]
        >>> __test_print(addr_dict['building'])
        [コスモタワー1001号室]

        >>> addr_dict = split_address(address_strs[3])
        >>> __test_print(addr_dict['address'])
        [高知県安芸市本町4-6-7]
        >>> __test_print(addr_dict['building'])
        [さざなみマンション502号室]

        >>> addr_dict = split_address(address_strs[4])
        >>> __test_print(addr_dict['address'])
        [高知県須崎市鍋島5-8-9]
        >>> __test_print(addr_dict['building'])
        [スプリングパレス201号]


            - 丁目、番地号が1つ以上ある場合に対応

        >>> addr_dict = split_address("安芸市本町4-6-7建物名Ａ")
        >>> __test_print(addr_dict['address'])
        [安芸市本町4-6-7]
        >>> __test_print(addr_dict['building'])
        [建物名Ａ]

        >>> addr_dict = split_address("安芸市本町4-5建物名Ｂ")
        >>> __test_print(addr_dict['address'])
        [安芸市本町4-5]
        >>> __test_print(addr_dict['building'])
        [建物名Ｂ]

        >>> addr_dict = split_address("安芸市本町2建物名Ｃ")
        >>> __test_print(addr_dict['address'])
        [安芸市本町2]
        >>> __test_print(addr_dict['building'])
        [建物名Ｃ]

        >>> addr_dict = split_address("安芸市本町4-5-3")
        >>> __test_print(addr_dict['address'])
        [安芸市本町4-5-3]
        >>> __test_print(addr_dict['building'])
        []

        >>> addr_dict = split_address("安芸市本町3-1")
        >>> __test_print(addr_dict['address'])
        [安芸市本町3-1]
        >>> __test_print(addr_dict['building'])
        []

        >>> addr_dict = split_address("安芸市本町5")
        >>> __test_print(addr_dict['address'])
        [安芸市本町5]
        >>> __test_print(addr_dict['building'])
        []

        >>> target_address = '広島県尾道市因島土生町中央区１７７－３２番'
        >>> addr_dict = split_address(target_address)
        >>> __test_print(addr_dict['address'])
        [広島県尾道市因島土生町中央区177-32]
        >>> __test_print(addr_dict['building'])
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

    if match := re.match(pattern, normalize_address(address_str)):
        # ディクショナリ形式で返却する
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

        >>> address_without_bld_name = "高知県四万十市中村一条"
        >>> addr_dict = ""
        >>> addr_dict = parse_chome_and_banchi(address_without_bld_name)
        >>> __test_print(addr_dict['location_base'])
        [高知県四万十市中村一条]
        >>> __test_print(addr_dict['chome'], addr_dict['banchi'],
        ...             addr_dict['gou'])
        [//]

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

    address_splited = dict(location_base="", chome="", banchi="", gou="")

    match = re.match(pattern, address_str)
    if match is None:
        # マッチしない場合は、引数文字列をそのまま返却する。
        address_splited['location_base'] = address_str
        return address_splited

    chome_banchi_gou = match.group(2).strip().split('-')

    address_splited['location_base'] = match.group(1).strip()
    if len(chome_banchi_gou) > 0:
        address_splited['chome'] = chome_banchi_gou[0]
    if len(chome_banchi_gou) > 1:
        address_splited['banchi'] = chome_banchi_gou[1]
    if len(chome_banchi_gou) > 2:
        address_splited['gou'] = chome_banchi_gou[2]

    return address_splited


def __test_create_address_prefix_file(test_addresses_file):
    '''__test_create_address_prefix_file

        テスト用に指定住所文字列を書き込んだファイルを作成する。

        >>> addr_file = "./test_addresses.txt"
        >>> __test_create_address_prefix_file(addr_file)
        >>> with open(addr_file, 'r') as f:
        ...     for line in f:
        ...         print(line, end="")
        広島県尾道市因島中庄町
        広島県尾道市因島土生町
        広島県尾道市西藤町
        広島県尾道市高須町

    '''
    addresses = [
        '広島県尾道市因島中庄町',
        '広島県尾道市因島土生町',
        '広島県尾道市西藤町',
        '広島県尾道市高須町'
    ]
    with open(test_addresses_file, 'w') as f:
        for line in addresses:
            f.write(f'{line}\n')

    return

def __get_prefixes_from_file(address_prefix_file: str) -> set:
    '''__get_prefixes_from_file

        指定住所文字列をファイルから取得する。読み込んだデータは空白を
        取り除き、重複排除して返却する。
        また、このデータはバイナリ形式でファイルに保存する。

        >>> addr_file = "./test_addresses.txt"
        >>> __test_create_address_prefix_file(addr_file)
        >>> prefs = __get_prefixes_from_file(addr_file)
        >>> '広島県尾道市西藤町' in prefs
        True
        >>> '広島県尾道市因島中庄町' in prefs
        True
        >>> '高知県高知市' in prefs
        False
    '''
    tmp_list = list()

    # 指定住所一覧ファイルを読み込む
    with open(address_prefix_file, 'r', encoding="utf-8") as f:
        for line in f:
            tmp_list.append(line.strip())

    prefixes = set(tmp_list)

    # キャッシュファイルに書き込む
    with shelve.open('./addr_prefs', 'c') as shelf_f:
        shelf_f['addr_prefs'] = prefixes

    return prefixes


def remove_extra_after_prefix(target_address: str):
    '''remove_extra_after_prefix

        指定された住所文字列（prefix）より後ろの余計な部分を削除する

        >>> target_address = '広島県尾道市因島中庄町油屋新開４８１５－１'
        >>> processed_addr = remove_extra_after_prefix(target_address)
        >>> __test_print(processed_addr)
        [広島県尾道市因島中庄町4815-1]

        >>> target_address = '広島県尾道市因島土生町中央区１７７－３２番'
        >>> processed_addr = remove_extra_after_prefix(target_address)
        >>> __test_print(processed_addr)
        [広島県尾道市因島土生町177-32]

        >>> target_address = '広島県尾道市因島土生町中央区１７７－３２しあわせ荘1'
        >>> processed_addr = remove_extra_after_prefix(target_address)
        >>> __test_print(processed_addr)
        [広島県尾道市因島土生町177-32 しあわせ荘1]

        >>> target_address = '広島県安芸市１７７－３２しあわせ荘1'
        >>> processed_addr = remove_extra_after_prefix(target_address)
        >>> __test_print(processed_addr)
        [広島県安芸市177-32 しあわせ荘1]

    '''
    # 指定住所一覧ファイルから指定住所を読み込む
    p_addr_prefs_text = Path('./address_prefixes.txt')
    p_addr_prefs_cache = Path('./addr_prefs')
    if p_addr_prefs_text.exists() is False:
        # 指定住所一覧ファイルがない場合、終了する
        return False
    if p_addr_prefs_cache.exists() is False:
        # キャッシュファイルがない場合は、ファイルから読み込む
        __get_prefixes_from_file(p_addr_prefs_text)
    else:
        # キャッシュファイルが存在する場合は、キャッシュから読み込む
        with shelve.open(p_addr_prefs_cache.name, 'r') as shelf_f:
            addr_prefs = shelf_f['addr_prefs']

    # 住所と建物名を分離する
    addr_dict = split_address(target_address)

    # 住所から丁目番地号を分離する
    parsed_address = parse_chome_and_banchi(addr_dict['address'])

    
    pref_matched = parsed_address['location_base']
    for pref in addr_prefs:
        if parsed_address['location_base'].startswith(pref) is False:
            continue
        else:
            pref_matched = pref
    
    # 指定住所文字列＋丁目番地号＋建物名
    processed_addr = pref_matched
    if len(parsed_address['chome']) > 0:
        processed_addr += f"{parsed_address['chome']}"
    if len(parsed_address['banchi']) > 0:
        processed_addr += f"-{parsed_address['banchi']}"
    if len(parsed_address['gou']) > 0:
        processed_addr += f"-{parsed_address['gou']}"
    if len(addr_dict['building']) > 0:
        processed_addr += f" {addr_dict['building']}"

    return processed_addr
