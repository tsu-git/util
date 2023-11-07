#!/usr/bin/python

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        prog = 'read_file',
        description = 'Read each line from a input file')
    parser.add_argument('filename', nargs=1)

    args = parser.parse_args()

    with open(*args.filename, "r") as f:
        for line in f:
            print(line, end='')
