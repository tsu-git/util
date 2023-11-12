#!/usr/bin/python
 
def show_all_keys(input_dict: dict, indent_depth: int = 0) -> bool:
    """Print all keys in the input_dict.

    input_dict:     json-format data.
    indent_depth:   define depth of indent. not mandatory.
    """

    each_indent = indent_depth
    indent_str = '    '

    for i, k in enumerate(input_dict.keys()):

        ind = indent_str * each_indent # make indent
        print('{0}{1} {2}'.format(ind, i, k))

        d = input_dict[k]
        if type(d) is not dict:
            continue
        else:
            each_indent += 1
            show_all_keys(d, each_indent)
        each_indent -= 1

    return(True)


if __name__ == "__main__":
    import argparse
    import sys
    import json

    parser = argparse.ArgumentParser(
        prog = 'print_all_json_keys',
        description = 'Read each line from a input file')
    parser.add_argument('infile', nargs=1, type=argparse.FileType("r"),
                        help='an input file to read')

    args = parser.parse_args()

    f = args.infile[0]
    d = json.load(f)

    show_all_keys(d)

    sys.exit()
