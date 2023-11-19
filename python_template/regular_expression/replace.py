#!/usr/bin/python

if __name__ == "__main__":
    import sys
    import re

    filename = "/c/Users/tsusu/python_training/json_sample/outfile.json"
    with open(filename, "r") as f:
        for line in f:
            if (matched := re.search('\".*労働力.*\"', line)):
                new_line = re.sub('労働力', '人間力', line)
                print(new_line)


    sys.exit()
