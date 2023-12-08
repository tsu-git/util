#!/usr/bin/python

if __name__ == "__main__":
    import sys
    import os
    from pathlib import Path
    import logging
    import argparse

    parser = argparse.ArgumentParser(
                prog='detail_f_list.py',
                description='show list bellow the given path')
    parser.add_argument('-d', '--debug', action='store_true',
                        help='print debug log')
    parser.add_argument('path', help='directory path')
    args = parser.parse_args()

    LOG_FMT = ' %(asctime)s: %(levelname)s: %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=LOG_FMT)

    if args.debug is False:
        logging.disable(logging.WARNING)

    path = args.path
    p = Path(path)
    logging.debug(f"p: {p}")
    logging.debug(f"Type of p: {type(p)}")

    if p.exists() is False:
        sys.exit(f"Not exists: [{str(p)}]")
    elif p.is_file():
        p = p.parent
        print("Use the parent path insted the received path")

    logging.debug(f"p: {p}")

    total_size = 0
    file_count = 0
    for f_obj in p.iterdir():
        if f_obj.is_file() is False:
            continue
        f_size = os.path.getsize(f_obj)
        print(f"{f_size:6d}: {f_obj}")
        total_size += f_size
        file_count += 1

    horizontal_sep = "-" * 70
    print(horizontal_sep)
    print(f"{total_size:6d}: {file_count} files")

    sys.exit()
