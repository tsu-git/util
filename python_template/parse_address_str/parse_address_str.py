'''parse_address_str.py

    住所文字列の解析、分割を行う。
'''
import re, doctest

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
    # ただし、直前の文字がカタカナに該当しない場合のみ
    address_converted = re.sub(r'(?<![ァ-ヶ])[－ー―−]', '-', address_converted)

    # 全角数字を半角に変換
    # TODO: 漢数字の対応を検討する
    address_converted = re.sub(r'[０-９]', lambda x: chr(ord(x.group(0)) - 0xFEE0), address_converted)

    # 丁目を半角ハイフンに変換
    address_converted = re.sub(r'丁目', '-', address_converted)
    # 番、番地を半角ハイフンに変換
    address_converted = re.sub(r'(番|番地)', '-', address_converted)
    # ハイフン＋数字＋号の「号」を除去する
    address_converted = re.sub(r'-\d+(号)', '', address_converted)

    return address_converted

def split_address(address_str)-> dict:
    '''split_address()
        
        引数の住所文字列から建物名を取り除く。
            - 番地号の後ろに続く建物名を削除する

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
        >>> addr = split_address(normalize_address(address_strs[0]))
        >>> print(addr['address'])
        高知県高知市本町1-1-1
        >>> print(addr['building'])
        サンライズビル301号室

        >>> addr = split_address(normalize_address(address_strs[1]))
        >>> print(addr['address'])
        高知県南国市後免町2-2-2
        >>> print(addr['building'])
        グリーンハイツＡ棟

        >>> addr = split_address(normalize_address(address_strs[2]))
        >>> print(addr['address'])
        高知県四万十市中村一条3-4-5
        >>> print(addr['building'])
        コスモタワー1001号室

        >>> addr = split_address(normalize_address(address_strs[3]))
        >>> print(addr['address'])
        高知県安芸市本町4-6-7
        >>> print(addr['building'])
        さざなみマンション502号室

        >>> addr = split_address(normalize_address(address_strs[4]))
        >>> print(addr['address'])
        高知県須崎市鍋島5-8-9
        >>> print(addr['building'])
        スプリングパレス201号


            - 丁目、番地号が1つ以上ある場合に対応

        >>> addr = split_address("安芸市本町4-6-7建物名Ａ")
        >>> print(addr['address'])
        安芸市本町4-6-7
        >>> print(addr['building'])
        建物名Ａ

        >>> addr = split_address("安芸市本町4-5建物名Ｂ")
        >>> print(addr['address'])
        安芸市本町4-5
        >>> print(addr['building'])
        建物名Ｂ

        >>> addr = split_address("安芸市本町2建物名Ｃ")
        >>> print(addr['address'])
        安芸市本町2
        >>> print(addr['building'])
        建物名Ｃ

        >>> addr = split_address("安芸市本町4-5-3")
        >>> print(addr['address'])
        安芸市本町4-5-3
        >>> print(f"[{addr['building']}]")
        []

        >>> addr = split_address("安芸市本町3-1")
        >>> print(addr['address'])
        安芸市本町3-1
        >>> print(f"[{addr['building']}]")
        []
        
        >>> addr = split_address("安芸市本町5")
        >>> print(addr['address'])
        安芸市本町5
        >>> print(f"[{addr['building']}]")
        []
        
    '''
    #address_witout_building = address_str.split()[0]

    # 丁目や番地号の形式にマッチする正規表現
    pattern = re.compile(r'''
        (.*?\d+(?:-\d+){0,2})   # 住所部分
        (.*)                    # 建物部分
        ''', re.VERBOSE)
    match = re.match(pattern, address_str)

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


def split_address_str(address_str)-> list:
    return address_splited
