#!/usr/bin/python

if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser(
        prog = 'read_file',
        description = 'Read each line from a input file')

    """ notice: Below code does not close the file automatically
               when something unexpected has come up. But Python garbage 
               collector destroy file descriptors after the running the 
               program, so you don't worry about that usually.
    """
            
    parser.add_argument('infile', nargs=1, type=argparse.FileType("r"),
                        help='an input file to read')
    parser.add_argument('--max_number', dest='max_num', default=30,
                        type=int, 
                        help='max line number the integers. '
                            'this program reads the file until the number'
                            'of line. Default value is 30.')

    args = parser.parse_args()

    f = args.infile[0]
    max_num = args.max_num
    i = 0

    for line in f:
        if i >= max_num:
            break
        print(line, end='')
        i+=1

    f.close()
