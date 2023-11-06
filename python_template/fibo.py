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

    if len(sys.argv) < 2:
        print("Usage: {0} number".format(sys.argv[0]))
        sys.exit(102)

    fib(int(sys.argv[1]))
    sys.exit(0)
