#!/usr/bin/python
"""Convert character encoding

    convert caracter encoding of input file to specific encoding.
    This tool doesn't modify the input file.
"""

if __name__ == "__main__":
    import sys
    import logging
    import argparse

    parser = argparse.ArgumentParser(
                prog='convert_chr_code.py',
                description='convert a character code')

    parser.add_argument('in_file', help='an input file to convert from')
    parser.add_argument('-i', '--input_codec', default='utf-8',
                        choices=['utf-8', 'shift_jis', 'euc_jp', 
                        'iso2022_jp'])
    parser.add_argument('-o', '--output_codec', default='utf-8',
                        choices=['utf-8', 'shift_jis', 'euc_jp',
                        'iso2022_jp'])
    parser.add_argument('-d', '--debug', action='store_true',
                        help='print debug log')
    args = parser.parse_args()

    I_CODEC = args.input_codec
    O_CODEC = args.output_codec
    EXT = ".txt"
    LOG_FMT = ' %(asctime)s: %(levelname)s: %(message)s'

    if args.debug is False:
        logging.disable(logging.WARNING)

    logging.basicConfig(level=logging.DEBUG, format=LOG_FMT)

    in_file = args.in_file
    out_file = in_file + "_" + O_CODEC + EXT

    with open(out_file, mode='w', encoding=O_CODEC) as out_f:
        with open(in_file, 'r', encoding=I_CODEC) as in_f:
            for line in in_f:
                logging.debug(f'input [{line}]')
                out_f.write(line)


    sys.exit()
