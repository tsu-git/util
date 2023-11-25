#!/usr/bin/python

if __name__ == "__main__":
    import sys
    import re
    #import pyperclip

    FMT_VALUE_ONLY      = 1
    IDX_VALUE_AFTER_KEY = 1
    IDX_VALUE_ONLY      = 0
    expression = ""
    
    sum = 0
    while True:
        line = list(input().strip().split())
        if len(line) < FMT_VALUE_ONLY:
            break
        elif len(line) > FMT_VALUE_ONLY:
            index = IDX_VALUE_AFTER_KEY
        else:
            index = IDX_VALUE_ONLY

        value = "".join(line[index:])
        if value.isdecimal():
            try:
                num = int(value)
            except ValueError:
                print(f"failed to convert to int. [{value}]",
                    file=sys.stderr)
                sys.exit(False)
        elif matched := re.search('^[\+\- ]*\d+[\+\- ]+\d+', value):
            try:
                num = eval(value)
            except NameError:
                print(f"received invalid expression [{value}]",
                    file=sys.stderr)
                sys.exit(False)
        else:
            print(f"received invalid data [{value}]", file=sys.stderr)
            sys.exit(False)

        if len(expression) < 1:
            expression = str(num)
        else:
            expression = expression + " + " + str(num)
        sum += num

    expression = str(sum) + " = " + expression
    print(expression)
    #pyperclip.copy(sum)
    """ pyperclip doesn't work on CYGWIN.
    """

    sys.exit(True)
