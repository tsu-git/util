#!/data/data/com.termux/files/usr/bin/python
'''print_utf8.py
    print UTF-8 code and 
    charactor
'''
import sys

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} expand_number")
    sys.exit()

expand_number = int(sys.argv[1])

for i in range(0x3040, 0x30A0 + expand_number):
    print(f"Unicode {i:#x}: {chr(i)}")
