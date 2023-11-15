#!/usr/bin/python
 
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

        if type(d) is str:
            # end point of this branch
            continue

        elif type(d) is list:
            print('{0}## list items >>'.format(ind))
            each_indent += 1
            prev_c_keys = {}

            for c in d:
                c_keys = { x for x in sorted(c.keys()) }

                #print(f"previous: {prev_c_keys}")
                #print(f"current: {c_keys}")

                if len(prev_c_keys) < 1 or len(c_keys ^ prev_c_keys) > 0:
                    duplicate_elem_num = 1
                    prev_c_keys = c_keys
                    show_all_keys(c, each_indent)
                else:
                    # both sets have same keys
                    prev_c_keys = c_keys
                    duplicate_elem_num += 1
                    #print(f"same keys. duplicate number[{duplicate_elem_num}]")
                    continue


            if duplicate_elem_num > 1:
                print(f"{ind}>> duplicate elements [{duplicate_elem_num}]")

            each_indent -= 1

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

    ret = show_all_keys(d)
    if not ret:
        print("Failed to call show_all_keys(), return[{0}]".format(ret))

    sys.exit()
