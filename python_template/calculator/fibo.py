#!/usr/bin/python

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

if __name__ == "__main__":
    import sys
    import re

    # check the number of arguments
    if len(sys.argv) < 2:
        print("Usage: {0} number".format(sys.argv[0]))
        sys.exit(100)

    n = sys.argv[1]

    # check if the string includes only digits
    match = re.fullmatch('[0-9]+', n)
    if not match:
        print("needs only integer!")
        print("Usage: {0} number".format(sys.argv[0]))
        sys.exit(101)

    fib(int(n))
    sys.exit(0)
