"""url_parser.py

    引数のURLを解析するスクリプト。pathとqueryについては、パーセント
    エンコードされた文字をUnicode文字に変換する。

    URLは引用符（"ないし'）で囲むこと。
"""
# coding: utf-8
import sys
from urllib.parse import urlparse, unquote

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} url")
    print("url sould be quated using \" or \'.")
    sys.exit()

url = sys.argv[1]

parsed_url = urlparse(url)
decoded_path = unquote(parsed_url.path)
decoded_query = unquote(parsed_url.query)

print(f"scheme: {parsed_url.scheme}")
print(f"net location: {parsed_url.netloc}")
print(f"path: {decoded_path}")
print(f"query: {decoded_query}")
