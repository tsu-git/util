#!/usr/bin/python
import unittest
import re

def regex_signed_integer():
    regex = '^[-+]?\d+$'
    return(regex)

def regex_signed_float():
    regex = '^[-+]?\d+\.\d+$'
    return(regex)

def regex_expression():
    regex = '^[-+]?\d+( *[-+] *\d+)+$'
    return(regex)

class TestRegularExpression(unittest.TestCase):
    
    def test_regex_signed_integer(self):
        value_list = ['7', '39', '-5', '+4']
        for value in value_list:
            matched = re.search(regex_signed_integer(), value)
            self.assertTrue(matched, True)

        value_list = ['1 + 2', '3.4', '0.5', '-1.5', '+44.2', 'a', 'x2']
        for value in value_list:
            matched = re.search(regex_signed_integer(), value)
            self.assertFalse(matched, True)
        
    def test_regex_signed_float(self):
        value_list = ['7.2', '0.39', '-5.2', '+0.4']
        for value in value_list:
            matched = re.search(regex_signed_float(), value)
            self.assertTrue(matched, True)

        value_list = ['1 + 2', '34', '05', '-15', '+442', 'a', 'x2']
        for value in value_list:
            matched = re.search(regex_signed_float(), value)
            self.assertFalse(matched, True)
        
    def test_regex_expression(self):
        value_list = ['1 + 2', '5+9', '32 - 4']
        for value in value_list:
            matched = re.search(regex_expression(), value)
            self.assertTrue(matched, True)

        value_list = ['12', '3.4', '05', '-15', '+442', 'a', 'x2']
        for value in value_list:
            matched = re.search(regex_expression(), value)
            self.assertFalse(matched, True)
        


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
        if matched := re.search(regex_signed_integer(), value):
            try:
                num = int(value)
            except ValueError:
                print(f"failed to convert to int. [{value}]",
                    file=sys.stderr)
                sys.exit(False)
        elif matched := re.search(regex_signed_float(), value):
            try:
                num = float(value)
            except ValueError:
                print(f"failed to convert to float. [{value}]",
                    file=sys.stderr)
                sys.exit(False)
        elif matched := re.search(regex_expression(), value):
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
