#!/usr/bin/python

import sys
import argparse

# 引数を取得する
parser = argparse.ArgumentParser(
            prog='stub_script.py',
            description='stub script for run_anotherScript.py'
        )
parser.add_argument('-f', '--file', help='configuration file')
parser.add_argument('--year_month', default="202401")
parser.add_argument('--date', default="1")
args = parser.parse_args()

print(f"received year_month: {args.year_month}")


sys.exit()
