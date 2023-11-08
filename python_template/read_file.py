#!/usr/bin/python

if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser(
        prog = 'read_file',
        description = 'Read each line from a input file')

    # notice: below code does not allow to close the file automatically
    parser.add_argument('infile', nargs=1, type=argparse.FileType("r"))

    args = parser.parse_args()

    f = args.infile[0]

    for line in f:
        print(line, end='')
    f.close()
