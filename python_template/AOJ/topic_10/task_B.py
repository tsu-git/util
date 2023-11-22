#!/usr/bin/python

if __name__ == "__main__":
    import sys
    import math

    prompt = "input length of a, length of b, angle: "

    a, b, C = map(float, input(prompt).strip().split())

    rad = math.radians(C)

    h = math.sin(rad) * b
    S = (a * h) / 2

    a_2 = math.cos(rad) * b
    a_1 = a - a_2

    length_c = math.sqrt(a_1 ** 2 + h ** 2)
    L = a + b + length_c

    print(f"{S:.5f}")
    print(f"{L:.5f}")
    print(f"{h:.5f}")

    sys.exit()

