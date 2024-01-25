#!/root/.pyenv/shims/python

"""is_strong_password

    引数として渡されたパスワードが強いかどうか判定する
"""

import re, sys

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} password")
    sys.exit()

password = sys.argv[1]

enough_len_regex = re.compile(r'\S{8,}')
enough_length = lambda password : enough_len_regex.search(password)

lower_case_regex = re.compile(r'[a-z]')
lower_case = lambda password : lower_case_regex.search(password)

upper_case_regex = re.compile(r'[A-Z]')
upper_case = lambda password : upper_case_regex.search(password)

digit_regex = re.compile(r'\d')
include_digit = lambda password : digit_regex.search(password)

if enough_length(password) is None:
    print(f"Need greater equal 8 byte [{password}]")
    sys.exit()

if lower_case(password) is None:
    print(f"Need lower case character at least more than one [{password}]")
    sys.exit()

if upper_case(password) is None:
    print(f"Need upper case character at least more than one [{password}]")
    sys.exit()

if include_digit(password) is None:
    print(f"Need digit at least more than one [{password}]")
    sys.exit()

