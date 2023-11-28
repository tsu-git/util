#!/usr/bin/python

if __name__ == "__main__":
    import sys
    import math

    prompt = "input two numbers (x, y): "

    x, y = map(int, input(prompt).strip().split())
    greate_common_div = math.gcd(x, y)

    print(greate_common_div)

    sys.exit()

