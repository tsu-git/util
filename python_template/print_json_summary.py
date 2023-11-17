#!/usr/bin/python
 
def show_values(input_dict: dict, indent_depth: int = 0) -> bool:
    """Print all values in the input_dict.

    input_dict:     json-format data.
    indent_depth:   define depth of indent. not mandatory.
    """

    if type(input_dict) is not dict or type(indent_depth) is not int:
        return(False)

    each_indent = indent_depth
    indent_str = ' ' * 4

    for k, v in input_dict.items():

        ind = indent_str * each_indent # make indent
        print('{0}{1}'.format(ind, k), end="")

        v = input_dict[k]

        if type(v) is not list and type(v) is not dict:
            # end point of this branch
            print(': {0}'.format(v))
            continue

        elif type(v) is dict:
            print()
            each_indent += 1
            show_values(v, each_indent)
            each_indent -= 1

        elif type(v) is list:
            print()
            print('{0}## list items >>'.format(ind))
            each_indent += 1
            prev_c_keys = {}

            for c in v:
                c_keys = { x for x in sorted(c.keys()) }

                if len(prev_c_keys) < 1 or len(c_keys ^ prev_c_keys) > 0:
                    duplicate_elem_num = 1
                    prev_c_keys = c_keys
                    show_values(c, each_indent)
                else:
                    # both sets have same keys
                    prev_c_keys = c_keys
                    duplicate_elem_num += 1
                    continue


            if duplicate_elem_num > 1:
                print(f"{ind}>> iterated elements [{duplicate_elem_num}]")

            each_indent -= 1

        else:
            print(f"invalid type of data [{v}]")


    return(True)


def show_all_keys(input_dict: dict, indent_depth: int = 0) -> bool:
    """Print all keys in the input_dict.

    input_dict:     json-format data.
    indent_depth:   define depth of indent. not mandatory.
    """

    if type(input_dict) is not dict or type(indent_depth) is not int:
        return(False)

    each_indent = indent_depth
    indent_str = ' ' * 4

    for i, k in enumerate(input_dict.keys()):

        ind = indent_str * each_indent # make indent
        print('{0}{1} {2}'.format(ind, i, k))

        d = input_dict[k]

        if type(d) is not list and type(d) is not dict:
            # end point of this branch
            continue

        elif type(d) is dict:
            each_indent += 1
            show_all_keys(d, each_indent)
            each_indent -= 1

        elif type(d) is list:
            print('{0}## list items >>'.format(ind))
            each_indent += 1
            prev_c_keys = {}

            for c in d:
                c_keys = { x for x in sorted(c.keys()) }

                if len(prev_c_keys) < 1 or len(c_keys ^ prev_c_keys) > 0:
                    duplicate_elem_num = 1
                    prev_c_keys = c_keys
                    show_all_keys(c, each_indent)
                else:
                    # both sets have same keys
                    prev_c_keys = c_keys
                    duplicate_elem_num += 1
                    continue


            if duplicate_elem_num > 1:
                print(f"{ind}>> iterated elements [{duplicate_elem_num}]")

            each_indent -= 1

        else:
            print(f"invalid type of data [{d}]")


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
    parser.add_argument('-k', '--key', type=str,
                        help='extract keys below the given key '
                            'in the data. use comma to seperate words '
                            'when you need to set multiple keys.')
    parser.add_argument('-v', '--value', action="store_true",
                        help='show value with key.')

    args = parser.parse_args()

    if args.key:
        keywords = list(args.key.strip().split(","))

    f = args.infile[0]
    d = json.load(f)

    if args.key:
        for i_key in keywords:
            if i_key not in d:
                print(f"{i_key} is not in the dictionary")
                sys.exit()
            d = d[i_key]

    if args.value:
        ret = show_values(d)
        if not ret:
            print("Failed to call show_values(), return[{0}]".format(ret))
    else:
        ret = show_all_keys(d)
        if not ret:
            print("Failed to call show_all_keys(), return[{0}]".format(ret))

    sys.exit()
