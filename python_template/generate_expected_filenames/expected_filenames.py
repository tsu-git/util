import unittest, re

def expected_file_pattern():
    patten = r"P\d\d_([^_.]+)_([^_.]+)\.[a-z]+"
    return(patten)

def mk_fileName_list(conf):
    ext = conf['extention'][0]
    fname_list = []

    for prefs in conf['prefs']:
        for direction in conf['direction']:
            for pressure in conf['pressure']:
                fname = f"P{prefs}_{direction}_{pressure}.{ext}"
                fname_list.append(fname)

    return(fname_list)

class test_class(unittest.TestCase):

    def test_mk_fileName_list(self):
        conf_json = {
                "prefs": ["21", "22", "23"],
                "direction": ["dem", "gen"],
                "pressure": ["hi", "lo"],
                "extention": [".csv"]
            }

        file_list = mk_fileName_list(conf_json)
        self.assertEqual(len(file_list), 12)

        for f in file_list:
            filename_regex = re.compile(expected_file_pattern())
            matched = filename_regex.findall(f)
            self.assertFalse(matched, True)


if __name__ == "__main__":
    unittest.main()

    import sys, json
    from pathlib import Path

    # 引数取得
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} conf_file")
        sys.exit()

    # 設定ファイル検査
    p = Path(sys.argv[1])
    if p.is_file() != True:
        print(f"{sys.argv[1]} isn't a file")
        print(f"Usage: {sys.argv[0]} conf_file")
        sys.exit()

    # 設定ファイル読込
    with open(p, "r", encoding="utf-8") as conf_fp:
        try:
            conf = json.load(conf_fp)
        except json.decoder.JSONDecodeError:
            print(f"{sys.argv[1]} isn't a valid json file")
            print(f"Usage: {sys.argv[0]} conf_file")
            sys.exit()

    # ファイル名生成
    file_name_list = mk_fileName_list(conf)

    # TODO: ファイル名出力
    for f in file_name_list:
        print(f)

sys.exit()
