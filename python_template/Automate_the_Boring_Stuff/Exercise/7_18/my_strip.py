"""my_strip

    正規表現を用いたstripメソッド
"""

import re

def strip(*args) -> str:
    targ_str = args[0]
    chars = None
    if len(args) > 1:
        chars = args[1]

    white_space_regex = re.compile(r"^\s*(\S+)\s*$")
    given_chars_regex = re.compile(f"^[{chars}]*(\w+?)[{chars}]*$")
    print(white_space_regex)
    print(given_chars_regex)
    if chars is None:
        replaced_str = white_space_regex.sub(r'\1', target_str)
    else:
        replaced_str = given_chars_regex.sub(r'\1', target_str)

    return(replaced_str)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} target_str chars")
        sys.exit()

    target_str = sys.argv[1]

    if len(sys.argv) > 2:
        chars = sys.argv[2]
        print(f"replaced string [{strip(target_str, chars)}]")
    else:
        print(f"replaced string [{strip(target_str)}]")
